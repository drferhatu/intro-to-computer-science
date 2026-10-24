// BMP-related data types based on Microsoft's own, as used in CS50.
// A 24-bit BMP file is: BITMAPFILEHEADER (14 bytes) + BITMAPINFOHEADER (40 bytes) + pixels,
// row by row from the BOTTOM of the image up, each pixel 3 bytes in the order blue, green, red,
// each row padded with zero bytes so that its length is a multiple of 4.

#include <stdint.h>

typedef uint8_t BYTE;
typedef uint32_t DWORD;
typedef int32_t LONG;
typedef uint16_t WORD;

typedef struct
{
    WORD bfType;
    DWORD bfSize;
    WORD bfReserved1;
    WORD bfReserved2;
    DWORD bfOffBits;
} __attribute__((__packed__)) BITMAPFILEHEADER;

typedef struct
{
    DWORD biSize;
    LONG biWidth;
    LONG biHeight;
    WORD biPlanes;
    WORD biBitCount;
    DWORD biCompression;
    DWORD biSizeImage;
    LONG biXPelsPerMeter;
    LONG biYPelsPerMeter;
    DWORD biClrUsed;
    DWORD biClrImportant;
} __attribute__((__packed__)) BITMAPINFOHEADER;

// One pixel: three bytes, blue first
typedef struct
{
    BYTE rgbtBlue;
    BYTE rgbtGreen;
    BYTE rgbtRed;
} __attribute__((__packed__)) RGBTRIPLE;
