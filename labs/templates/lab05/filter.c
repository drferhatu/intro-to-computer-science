// Part D · filter.c
// Apply a filter to a 24-bit BMP image:
//
//   $ make filter
//   $ ./filter grayscale images/firat.bmp images/out-gray.bmp
//   $ ./filter reflect   images/firat.bmp images/out-mirror.bmp
//
// main (written for you) checks the arguments, reads the headers, loads the pixels into
// image[height][width] (one RGBTRIPLE per pixel), calls your filter, and writes the result.
// You write the two filters:
//   grayscale: every pixel's red, green and blue become the rounded average of the three
//              (use round() from <math.h> on (r + g + b) / 3.0); a gray pixel has r == g == b.
//   reflect:   mirror each row horizontally: swap the first and last pixel, the second and
//              second-to-last, and so on (swapping a whole RGBTRIPLE at once is fine).
// Do not touch main; the checks compare your output pixels with the expected ones.

#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "bmp.h"

void grayscale(int height, int width, RGBTRIPLE image[height][width]);
void reflect(int height, int width, RGBTRIPLE image[height][width]);

int main(int argc, char *argv[])
{
    if (argc != 4 || (strcmp(argv[1], "grayscale") != 0 && strcmp(argv[1], "reflect") != 0))
    {
        printf("Usage: ./filter grayscale|reflect infile outfile\n");
        return 1;
    }

    FILE *inptr = fopen(argv[2], "rb");
    if (inptr == NULL)
    {
        printf("Could not open %s.\n", argv[2]);
        return 2;
    }
    FILE *outptr = fopen(argv[3], "wb");
    if (outptr == NULL)
    {
        fclose(inptr);
        printf("Could not create %s.\n", argv[3]);
        return 3;
    }

    // Read the two headers
    BITMAPFILEHEADER bf;
    BITMAPINFOHEADER bi;
    fread(&bf, sizeof(BITMAPFILEHEADER), 1, inptr);
    fread(&bi, sizeof(BITMAPINFOHEADER), 1, inptr);

    // Only uncompressed 24-bit BMP 4.0 files are supported
    if (bf.bfType != 0x4d42 || bf.bfOffBits != 54 || bi.biSize != 40 || bi.biBitCount != 24 || bi.biCompression != 0)
    {
        fclose(outptr);
        fclose(inptr);
        printf("Unsupported file format.\n");
        return 4;
    }

    int height = abs(bi.biHeight);
    int width = bi.biWidth;

    // Pixels, as a 2-D array on the heap
    RGBTRIPLE(*image)[width] = calloc(height, width * sizeof(RGBTRIPLE));
    if (image == NULL)
    {
        printf("Not enough memory to store image.\n");
        fclose(outptr);
        fclose(inptr);
        return 5;
    }

    // Each row is padded to a multiple of 4 bytes
    int padding = (4 - (width * sizeof(RGBTRIPLE)) % 4) % 4;

    for (int i = 0; i < height; i++)
    {
        fread(image[i], sizeof(RGBTRIPLE), width, inptr);
        fseek(inptr, padding, SEEK_CUR);
    }

    if (strcmp(argv[1], "grayscale") == 0)
    {
        grayscale(height, width, image);
    }
    else
    {
        reflect(height, width, image);
    }

    // Write headers, then pixels with padding
    fwrite(&bf, sizeof(BITMAPFILEHEADER), 1, outptr);
    fwrite(&bi, sizeof(BITMAPINFOHEADER), 1, outptr);
    for (int i = 0; i < height; i++)
    {
        fwrite(image[i], sizeof(RGBTRIPLE), width, outptr);
        for (int k = 0; k < padding; k++)
        {
            fputc(0x00, outptr);
        }
    }

    free(image);
    fclose(inptr);
    fclose(outptr);
    return 0;
}

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // TODO
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // TODO
}
