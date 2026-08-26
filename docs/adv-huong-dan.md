# adv — Hướng dẫn

Vòng lặp làm khó đề: GPT-5.5 medium giải mù, chat Sol đã tạo đề đó chấm. Giải
được → đề dễ → Sol harden → lặp. Giải không được → PASS.

Cả hai model đều chạy trên ChatGPT web do bạn điều khiển, nên dùng quota chat
miễn phí của gói Plus. `adv` **không** đụng vào chatgpt.com — nó chỉ đọc/ghi
clipboard máy bạn, định tuyến từng câu trả lời về đúng problem, và ghi file.

---

## 1. Danh sách lệnh

Chạy từ thư mục repo: `cd ~/workspace/freelance/hd-techlabs-math-skills-copy`

### `./scripts/adv watch`

Bật daemon rình clipboard. **Phải chạy suốt** trong một cửa sổ terminal riêng.

Mỗi lần bạn bấm nút **Copy** trong ChatGPT, nó tự nhận diện, ghi file, tăng
vòng, và in ra bước tiếp theo. Không bật thì bấm Copy chẳng ai hứng.

Sửa `scripts/adv` xong phải `Ctrl+C` rồi bật lại — Python nạp file một lần lúc
khởi động, daemon cũ vẫn chạy code cũ. `adv status` sẽ cảnh báo khi phát hiện.

### `./scripts/adv add [--force] <slug>...`

Đưa problem vào hàng đợi theo dõi. Thêm lúc nào cũng được, một hay nhiều cái.

```bash
./scripts/adv add problem88
./scripts/adv add problem90 problem91
```

Trước khi đăng ký, `adv` chạy `git fetch origin` và so folder problem đó với **mọi
remote ref**. Nếu trên GitHub có commit chạm folder mà working tree chưa có (sửa ở
clone khác, hoặc nằm ở branch PR chưa merge) thì nó **từ chối** — vì mọi thứ trong
`adv` đều đọc working tree, đăng ký lúc đó là chạy cả vòng lặp trên bản đã lỗi thời.
Pull/checkout rồi add lại, hoặc `--force` nếu cố ý dùng bản local.

Định danh là **số** (`problem88`), không phải tên đầy đủ. Hậu tố domain đổi thế
nào cũng không ảnh hưởng.

Bắt buộc phải có `problem.md`. Thiếu `solution.md` vẫn thêm được — khi đó chạy ở
chế độ "chat giữ ground truth", Sol sẽ được yêu cầu tự xuất `solution.md`.

### `./scripts/adv brief <slug>`

Nạp **hợp đồng đầu ra** vào clipboard. Dán **một lần duy nhất** vào chat Sol của
problem đó, lúc mới mở chat.

Nó dạy Sol: trả lời theo marker `=== VERDICT: ===`, bọc file trong fence
` ```markdown `, giữ cấu trúc `solution.md`, đọc skill nào trước khi harden.

Sau đó mỗi vòng chỉ cần dán lời giải trần, không phải nhắc lại.

Chạy lại nếu chat dài làm Sol quên format, hoặc bạn mở chat Sol mới.

### `./scripts/adv next <slug>`

Nạp **đề bài** vào clipboard, để dán cho GPT-5.5.

Chỉ trích phần `## LaTeX (Normalized)` — cắt bỏ Domain Classification và Domain
Explanation vì hai phần đó lộ hướng giải.

Nếu problem đang chờ Sol chấm, lệnh này không nạp gì, chỉ nhắc bạn dán lời giải
sang chat Sol.

### `./scripts/adv attempt <slug>`

Nạp lại **lời giải của 5.5 đã hứng** vào clipboard.

Dùng khi clipboard bị ghi đè giữa chừng (chạy lệnh khác, copy thứ khác) mà bạn
chưa kịp dán sang chat Sol.

### `./scripts/adv format <slug>`

Nạp yêu cầu **viết lại `solution.md` đúng chuẩn repo** vào clipboard. Dán vào
chat Sol.

Sol sẽ đọc `skills/format-solution/SKILL.md`, `style_guide.md`,
`blocked_words.md` từ GitHub rồi format lại — **không đổi toán học, không đổi
đáp án**.

Chạy được ở mọi trạng thái, kể cả problem đã PASS. Không làm lệch vòng lặp. Bản
cũ giữ ở `versions/solution.preformat-rN.md`.

### `./scripts/adv status`

Bảng tổng: problem nào ở vòng mấy, đang chờ gì, lần cuối động vào khi nào.

```
SLUG        ROUND  WAITING FOR   LAST
problem88       3  Sol check     2m ago
problem90       1  5.5 solve     —
problem75       2  PASS ✓        7m ago
```

`5.5 solve` = tới lượt dán đề cho 5.5. `Sol check` = tới lượt dán lời giải cho
Sol.

### `./scripts/adv catch <slug>`

Ép nội dung clipboard hiện tại về problem đó, bỏ qua bước đọc tag.

Dùng khi Sol quên chép dòng `=== PROBLEM: ... ===` nên daemon báo `ignored`.
Clipboard vẫn phải chứa marker verdict.

### `./scripts/adv redo <slug>`

Vứt lời giải đã hứng, quay về bước 5.5 giải.

Dùng khi lời giải đó vô giá trị — giải nhầm phiên bản đề, hoặc bị nát công thức.
Mở lại được cả problem đã PASS.

### `./scripts/adv reseed <slug>`

Đánh dấu: lần tới gửi Sol thì nhúng kèm toàn bộ `problem.md` + `solution.md`.

Phần lớn trường hợp không cần gõ lệnh này: `adv` băm `problem.md` + `solution.md`
mỗi lần đưa cho một chat, và tự nhúng lại khi không chứng minh được chat đang
giữ đúng cặp file đó — sau `adv add`, sau khi sửa đề theo reviewer ở chat khác,
sau khi sửa tay, `git pull`, hay merge PR. `reseed` chỉ là ép thủ công.

Dùng khi mất chat Sol gốc và phải mở chat mới — chat mới không có context nên
cần được nạp lại.

### `./scripts/adv show <slug>`

In state chi tiết và lịch sử từng vòng của một problem.

### `./scripts/adv drop <slug>...`

Gỡ khỏi hàng đợi theo dõi. **Không xoá** `problem.md`, `solution.md` hay lưu
vết. Thêm lại thì bắt đầu từ vòng 1.

---

## 2. Biến môi trường

| Biến | Tác dụng |
|---|---|
| `ADV_NO_PUSH=1` | commit local nhưng **không push**. Dùng khi thử nghiệm |
| `ADV_STATE=<đường dẫn>` | dùng state khác, không đụng bảng thật |
| `ADV_EMBED=1` | ép nhúng nội dung thay vì trỏ GitHub |

---

## 3. Quy trình làm việc

### Chuẩn bị đầu ngày

```bash
cd ~/workspace/freelance/hd-techlabs-math-skills-copy
git pull                    # phòng máy/agent khác đã đẩy
./scripts/adv watch         # terminal A, để nguyên cả ngày
```

Terminal B dùng cho mọi lệnh còn lại.

### Đưa một problem vào vòng lặp

```bash
./scripts/adv add problem88
./scripts/adv brief problem88     # dán 1 lần vào chat Sol của problem88
```

Đổi tên chat Sol trên ChatGPT thành `problem88` cho dễ tìm.

### Mỗi vòng — 2 lần dán

**Bước 1. Đề cho 5.5**

```bash
./scripts/adv next problem88
```

Mở **Temporary Chat MỚI** (biểu tượng ⧉), chọn GPT-5.5 Thinking/medium,
`Ctrl+V`, Enter. Xong bấm **Copy**.

```
[adv] problem88: solver attempt captured (round 1)
```

**Bước 2. Lời giải cho Sol**

Dán thẳng vào **chat Sol cũ** của problem88. Enter. Xong bấm **Copy**.

Clipboard đã bị ghi đè? `./scripts/adv attempt problem88` để lấy lại.

**Bước 3. Máy tự xử**

```
[adv] problem88: TOO_EASY → hardened, now round 2, pushed  → quay lại bước 1
[adv] problem88: PASS after 2 round(s)                     → xong
```

### Khi PASS

```bash
./scripts/adv format problem88     # viết lại solution.md đúng chuẩn repo
git push origin main               # nếu chưa tự push
```

---

## 4. Quy tắc bắt buộc

| | Quy tắc | Vì sao |
|---|---|---|
| Chat 5.5 | **Temporary Chat, mới mỗi vòng** | không được nhớ gì; vòng trước hoặc chat Sol lọt vào là nó chép bài |
| Chat Sol | **giữ nguyên một chat xuyên suốt** | phải nhớ đã bịt route nào |
| Project | **5.5 không được ở trong project nào** | chat cùng project đọc được nhau |
| Sửa `scripts/adv` | **restart `adv watch`** | daemon giữ code cũ trong bộ nhớ |

Hai chat ngược nhau hoàn toàn. Nhầm chiều nào cũng hỏng tín hiệu.

---

## 5. Xử lý sự cố

| Thông báo / hiện tượng | Nguyên nhân | Cách xử |
|---|---|---|
| `ignored: reply carries no '=== PROBLEM: ... ===' tag` | Sol quên chép tag | `adv catch <slug>` |
| `clipboard holds no ... marker` | clipboard đã bị ghi đè | quay lại chat, bấm Copy lại, chạy `catch` ngay |
| `refused: solution.md is missing ## Answer, ## Classification` | Sol trả thiếu section | bảo Sol gửi lại đủ; **chưa ghi gì cả** |
| `refused: TOO_EASY but the reply carried ['problem.md']` | reply bị cắt giữa chừng | bảo Sol gửi lại đủ 2 file |
| `refused: <slug> awaits a solver attempt, not an author verdict` | dán nhầm bước | xem `adv status` |
| `error: <folder>: a newer version of this problem exists on the remote` | bản mới nhất nằm trên GitHub (clone khác, hoặc branch PR chưa merge), working tree đang giữ bản cũ | `git pull --rebase origin main`, hoặc `git checkout <branch>`, rồi `adv add` lại. Cố tình dùng bản local: `adv add <slug> --force` |
| `refused: the author chat says it does not hold the current <slug>` | chat Sol và repo lệch phiên bản | `adv reseed` rồi dán lại |
| `refused: the current problem.md and solution.md were pasted into that chat ...` | đã nhúng file hiện tại mà Sol vẫn trả STALE → chat trả lời theo trí nhớ cũ | **không ghi gì cả**; mở chat Sol mới: `adv reseed <slug> && adv next <slug>` |
| `<slug>: the Sol chat has not been sent the current problem.md ... Use: adv next` | gõ `adv attempt` khi chat chưa có file hiện tại | dùng `adv next <slug>` — nó dán kèm file |
| `warning: the attempt has N mangled formula line(s)` | 5.5 để `=` đầu dòng, copy làm nát | dùng được nếu đáp án còn nguyên, không thì `adv redo` |
| `warning: the running 'adv watch' started before this script was last edited` | daemon chạy code cũ | restart daemon |
| `error on <slug>: ...` | lỗi ngoài dự kiến | xem `.tmp/adv/last-error.txt`, daemon vẫn chạy tiếp |
| Copy xong daemon im lặng | daemon chết hoặc chưa bật | kiểm tra terminal A |

---

## 6. Dữ liệu nằm đâu

```
.tmp/adv/
  state.json                        bảng theo dõi (gitignore, chỉ máy này)
  last-error.txt                    traceback lần lỗi gần nhất
  <slug>/
    attempt.md                      lời giải 5.5 mới nhất
    round01-attempt.md              lời giải từng vòng
    round01-verdict.md              verdict từng vòng
    versions/problem.r1.md          đề trước mỗi lần harden
    versions/solution.preformat-r1.md   solution trước khi format
```

Sống qua tắt máy vì là file trên đĩa. Nhưng `.tmp/` bị gitignore nên **chỉ nằm
trên máy này** — đổi máy là mất bảng theo dõi (`problem.md`/`solution.md` vẫn
còn vì nằm trong git).

Mỗi lần harden cũng là một commit, nên `git log -- <thư mục problem>` là lịch sử
tiến hoá của đề đó.

---

## 7. Những gì `adv` tự chặn

Nó **từ chối** thay vì đoán:

- clipboard không có tag → bỏ qua
- slug chưa đăng ký → bỏ qua
- dán nhầm giai đoạn → từ chối
- copy trùng một reply hai lần → bỏ qua
- `TOO_EASY` mà thiếu file → **không ghi gì cả**
- `solution.md` thiếu `## Answer` / `## Classification` → từ chối
- chính prompt của nó bị copy lại → bỏ qua (nhờ dấu `=== ADV-PROMPT ===`)

Và tự làm:

- đổi tên folder theo `Sub-domain` mới sau mỗi lần harden
- lưu bản cũ vào `versions/` trước khi ghi đè
- commit + push mỗi lần đổi file
