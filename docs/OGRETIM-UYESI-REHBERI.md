# Öğretim üyesi rehberi · Introduction to Computer Science (YMT113) sitesi ve lab sistemi

Bu belge yalnızca size yönelik bakım notudur (öğrenciler siteyi görür, bu dosyayı değil).
Site: `https://drferhatu.github.io/intro-to-computer-science/` · Depo: `drferhatu/intro-to-computer-science`
Discrete Mathematics sitesiyle aynı altyapı; farklar: C tabanlı lab şablonu, CS50 "Before class" kutusu, proje kataloğu sayfası.

---

## 1. Genel mimari

| Parça | Nerede | Ne işe yarar |
|---|---|---|
| Ders sitesi | bu depo, GitHub Pages | Haftalar, lab talimatları, proje kataloğu, duyurular (Astro + Tailwind + Pagefind) |
| CS50 bağlantıları | `content/weeks/week-NN.md → cs50:` | Her haftanın "Before class" kutusu: Malan'ın videosu, notlar, slaytlar, kaynak kod, pset |
| Lab şablonları | `labs/templates/labNN/` → org'da ayrı **template repo** | Lab 1: Scratch linkleri + `answers.txt` + `pseudocode.txt` (C yok). Lab 2+: C kodu, mini `cs50.h/cs50.c`, `Makefile`, testler, `check.py`, keşif defteri, `.devcontainer` |
| Autograder | `labs/autograders/labNN/tests.json` → Classroom 50 assignment ayarı | Her push'ta pytest (gcc ile derleyip çalıştırır), puan GitHub Release olarak yayımlanır |
| Classroom 50 | classroom50.org + `FiratUniversity-IJDP-SoftEng` org'u, sınıf `ics-2026` | Roster, ödev kabulü, öğrenci repoları, puan toplama (CSV) |
| Editör | GitHub Codespaces (öğrencinin kendi reposundan) | Tarayıcıda VS Code; `.devcontainer/setup.sh` gcc, make, gdb, valgrind, pytest kurar |
| Defterler | `notebooks/` (hafta) ve `labs/templates/labNN/labNN.ipynb` (lab) | `%%writefile` + `!gcc` ile C'yi Colab'da çalıştırır; `scripts/build_notebooks.py` HTML'e çevirir |
| Proje | `content/data/projects.json` → `/project` | 20 proje, 6 tema, min/ileri kapsam, kilometre taşları, rubrik, commit takibi kuralları |
| Gizli materyal | `private/` (**.gitignore'da**) | Lab çözümleri (`private/solutions/labNN/`). Asla GitHub'a gitmez |

---

## 2. Bir kerelik kurulum

### 2.1 Siteyi yayımlamak (yapıldı)

```bash
cd ".../Courses/ICS/site"
gh repo create drferhatu/intro-to-computer-science --public --source . --push
gh api -X POST repos/drferhatu/intro-to-computer-science/pages -f build_type=workflow
```

Her `git push` siteyi 2–3 dakikada yeniler (Actions → "Deploy to GitHub Pages").

### 2.2 Classroom 50 (GitHub Education onayı geldikten sonra, ~72 saat)

Org `FiratUniversity-IJDP-SoftEng` zaten Discrete Math için hazırlanıyor; aynı org'da ikinci bir sınıf açmanız yeter.

1. Education benefits → org'u **GitHub Team**'e ücretsiz yükseltin (bir kez, iki ders için ortak).
2. https://classroom50.org → org → **Set up organization** (DM için yaptıysanız atlayın).
3. **Create classroom** → kısa ad: **`introduction-to-computer-science`** (açıldı; `content/data/course.json → classroom.slug` ile aynı olmalı).
4. **Roster → Invite**: öğrenci e-postaları. DM ile ortak öğrenciler zaten org üyesi olacaktır.
5. Codespaces: org **Settings → Codespaces** → "Enable for all members", **ownership: user**.

### 2.3 Bir labı açmak (Lab 2 için yapıldı: `publish_lab_template.sh lab02` + `gh teacher assignment add … --tests labs/autograders/lab02/tests.json`; roster `gh teacher roster import … private/roster/ymt113-roster.csv`)

```bash
cd ".../Courses/ICS/site"
/opt/miniconda3/envs/ferhat_ml/bin/python scripts/verify_lab.py lab01      # starter 0/7, solution 7/7 olmalı
scripts/publish_lab_template.sh lab01                                        # org'da özel template repo: ics-2026-lab01-template
```

classroom50.org → `introduction-to-computer-science` → **New assignment** (ya da `gh teacher assignment add`):

- Slug: `lab01` · Name: `Lab 1 · Hello, Scratch` · Type: Individual
- Template: `FiratUniversity-IJDP-SoftEng/ics-2026-lab01-template`
- Grading: **Autograded** · Submission type: **Every push** · Due: 4 Ekim 23:59
- Autograding tests: `labs/autograders/lab01/tests.json` içeriği (tek pytest testi, 10 puan; runner'da gcc hazır)
- Kaydedin, **accept link**'i `content/labs/lab-01.mdx → acceptUrl` alanına yapıştırıp push edin.

**Test öğrenci hesabıyla deneyin**: kabul → Codespace (ilk açılış ~1 dk) → `python3 check.py` → push → Releases'ta puan.

### 2.4 (eski yedek plan; yerine 2b kullanılıyor)

Lab sayfası ve duyuru bunu öngörüyor. O gün için:

1. Şablonu geçici olarak **public** bir repoya koyun: `gh repo create drferhatu/ics-2026-lab01-starter --public --source labs/templates/lab01 --push` (gitignore'lı dosyalar hariç).
2. Öğrenciler **cs50.dev**'de terminale `git clone https://github.com/drferhatu/ics-2026-lab01-starter lab01 && cd lab01 && pip install pytest` yazar; cs50.dev'de gcc, clang ve make hazırdır.
3. `python3 check.py` yerelde çalışır; teslim için öğrenciler zip ya da kendi GitHub repolarına push eder; Classroom 50 açılınca aynı dosyaları oraya taşırlar (`acceptUrl` dolunca sayfadaki buton canlanır).

---

## 2b. B planı: Classroom 50 olmadan (Lab 1'de kullanılıyor)

Lab sayfasında `mode: template` yazıyorsa öğrenciler şu yolu izler: public şablondan kendi hesabında **özel**
`ics-2026-labNN` deposunu açar ("Create your copy" düğmesi → GitHub'ın "Use this template" formu), `drferhatu`'yu
collaborator ekler, README'ye ad/numara yazar, Codespaces'te (ya da doğrudan github.com'da kalemle) dosyaları düzenler, push eder.
Şablondaki `.github/workflows/check.yml` her push'ta testleri öğrencinin reposunda çalıştırır (commit yanında ✅/❌).
Org içindeki (Classroom 50) repolarda bu workflow kendini atlar. Lab 1'de C yok, sadece Python testleri; öğrencinin
Codespaces kotası bitse bile üç dosya github.com'da düzenlenebilir.

Hazırlık (yapıldı): `scripts/publish_lab_template.sh lab01 --public` → `FiratUniversity-IJDP-SoftEng/ics-2026-lab01-template` (public, template).

Teslim tarihinden sonra (Cumartesi), tek komut:

```bash
/opt/miniconda3/envs/ferhat_ml/bin/python scripts/collect_lab.py lab01          # son teslim lab sayfasından okunur (Cuma 23:59)
```

- `ics-2026-lab01` adlı depoların bekleyen collaborator davetlerini kabul eder (başka davetlere dokunmaz).
- Her depoda teslim tarihinden önceki **son push**'u GitHub'ın workflow kaydından bulur (commit tarihi taklit edilebilir, bu edilemez).
- O commit'i klonlar, `tests/` klasörünü **resmi testlerle** değiştirir, pytest çalıştırır.
- 5 güne kadar geç push'lara günlük %10 kesinti uygular (`--late-days`).
- `private/grades/lab01.csv` yazar (GitHub'a gitmez): github, ad, numara, puan, teslim saati, not.
- Scratch projelerine göz atmak için CSV'deki repo README'lerini açın; linkler oradadır.

Öğrenci kodu sizin bilgisayarınızda (geçici klasörde, GitHub token'ı olmadan, zaman aşımıyla) çalışır.
Belirli depoları denemek için: `--repos kullanici/ics-2026-lab01`.

Classroom 50 açılınca: lab sayfasında `mode: template` satırını silin (varsayılan classroom50), `acceptUrl` doldurun. Şablon repo aynen kalır.

## 3. Haftalık akış

1. **Hafta sayfası**: `content/weeks/week-NN.md(x)`. `cs50:` bloğu ve `prep:` listesi zaten dolu; notlar bitince `status: ready`.
   - `week-02.mdx` ve `week-03.mdx` tam notlu; 4–15 "outline" (Topics listesi). Notları yazarken 2–3'ün yapısını kopyalayın:
     `## …` başlıklar, `> [!definition]`, `> [!warning]`, `> [!try]`, `> [!why]`, `> [!industry]` kutuları, `<table class="bits">` ikili tablolar.
   - Kendi slaytlarınız: PDF'i `public/slides/` altına koyup frontmatter'da `slides: [{title, file}]`.
2. **Yeni lab**: `labs/templates/labNN/` (lab01'i kopyalayın: `cs50.h/.c`, `Makefile`'daki `PROGRAMS`, `tests/`, README), çözümü `private/solutions/labNN/`.
   Defter için `scripts/build_notebooks.py → NOTEBOOKS` sözlüğüne hücre listesi ekleyin.
3. `verify_lab.py labNN` → `publish_lab_template.sh labNN` → Classroom 50'de assignment.
4. `content/labs/lab-NN.md(x)`: `status: open`, `due`, `acceptUrl`; adımları `<Step>` ve `<Terminal>` ile Lab 1 gibi yazın (dosya `.mdx` olmalı).
5. **Duyuru**: `content/announcements/YYYY-MM-DD-ad.md` (`kind: info | important | exam | lab | project`, `pinned: true`).
6. **Puanlar**: classroom50.org → assignment → **Collect now** → CSV.

Tarih/tatil/sınav: `content/data/schedule.json` (`status: normal | holiday | postponed | exam`). Final tarihi `finals.date`.

Yerel önizleme:

```bash
export PATH=/opt/homebrew/bin:$PATH
npm run dev          # http://localhost:4321/intro-to-computer-science/
npm run build && /opt/miniconda3/envs/ferhat_ml/bin/python scripts/validate_content.py
```

---

## 4. Proje (%15 final)

- Fikir bankası **gizli**: `private/project-ideas.json` (20 proje, 6 tema, min/ileri kapsam). Sitede yalnızca çerçeve var (`/project`): tema adları, kilometre taşları, rubrik, commit takibi. Proje başlıkları ve kapsamlar yayımlanmaz.
- Atama: 5. hafta (19 Ekim). Sınıf listesi gelince projeleri rastgele dağıtacağız (bir projeye en fazla 2 öğrenci, farklı ileri kapsam); her öğrenciye kişisel duyuru/e-posta ile başlığı + min/ileri kapsamı gider. Dağıtım için küçük bir script yazılacak (`scripts/assign_projects.py`, roster CSV → atama CSV, `private/` altında).
- Depo: Classroom 50 açıksa şablonsuz bireysel `project` ödevi (Manual grading); değilse Lab 1'deki gibi öğrenci kendi hesabında özel `ics-2026-project` deposu açar, `drferhatu`'yu ekler.
- Kilometre taşları sitede: H2 çerçeve · H5 atama + ilk commit · H11 (30 Kasım) `m3-prototype` etiketi · H14 atölye · H15 (28 Aralık) demo + `v1.0`.
- Commit takibi için hızlı komut (öğrenci reposunda): `gh api repos/ORG/REPO/commits --paginate --jq '.[].commit.author.date' | cut -c1-10 | sort | uniq -c`.
- Süreç notu (%15): haftalık commit, etiketler, README görev listesi. Rubrik sitede.

## 5. Sık sorunlar

| Belirti | Neden / çözüm |
|---|---|
| Öğrenci "Not a member yet" görüyor | Org davetini kabul etmemiş ya da farklı GitHub hesabıyla girmiş. Roster'da e-postayı kontrol edin. |
| Accept 404 | Template özel ve assignment'ı bir **org owner** kaydetmedi. Assignment'ı açıp yeniden kaydedin. |
| `gcc: command not found` (codespace) | `setup.sh` bitmemiş; `bash .devcontainer/setup.sh`. |
| Testler "cs50.h not found" | `Makefile` ve `tests/conftest.py` `-I.` ile derler; dosya şablonda olmalı. |
| Puan çıkmıyor | Öğrenci reposunda Actions sekmesi; kırmızıysa log. Classroom 50'de "Collect now". |
| Defter HTML'i eski | `python scripts/build_notebooks.py --execute --force` (force, elle düzenlenmiş defteri ezer). |
