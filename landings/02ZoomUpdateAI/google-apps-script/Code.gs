/**
 * ABM · Form đăng ký Zoom 02 buổi → Google Sheet
 * Landing: https://pb.abmedu.vn/02ZoomUpdateAI/
 *
 * Cách dùng: mở Google Sheet đích → Tiện ích mở rộng → Apps Script → dán file này
 * → chạy hàm setup() một lần → Triển khai → Tùy chọn triển khai mới → Ứng dụng web
 * (Thực thi với tư cách: Tôi · Người có quyền truy cập: Bất kỳ ai) → copy URL /exec
 * → dán vào biến FORM_ENDPOINT trong index.html.
 */

// Để trống nếu script được gắn trực tiếp vào Sheet (khuyến nghị).
var SHEET_ID = '1hDdsO8Nx1HYpkWpSNp4TlUt15wysgtQQ_Via4gJFzUs';
// Email nhận thông báo khi có lead mới. Để trống = tắt.
var NOTIFY_EMAIL = '';

var HEADERS = ['Thời gian', 'Họ và tên', 'Số điện thoại', 'Email', 'Vai trò', 'Buổi tham gia',
  'Việc muốn áp dụng A.I', 'Đồng ý liên hệ', 'utm_source', 'utm_medium', 'utm_campaign',
  'Trang', 'Mã đăng ký', 'Trạng thái xử lý', 'Ghi chú'];

function getSheet_() {
  var ss = SHEET_ID ? SpreadsheetApp.openById(SHEET_ID) : SpreadsheetApp.getActiveSpreadsheet();
  return ss.getSheets()[0];
}

/** Chạy tay một lần: chuẩn hóa tiêu đề, định dạng cột, cố định hàng đầu. */
function setup() {
  var sh = getSheet_();
  sh.getRange(1, 1, 1, HEADERS.length).setValues([HEADERS])
    .setFontWeight('bold').setBackground('#030548').setFontColor('#ffffff');
  sh.setFrozenRows(1);
  sh.getRange('C:C').setNumberFormat('@');   // giữ số 0 đầu của SĐT
  sh.getRange('M:M').setNumberFormat('@');
  sh.autoResizeColumns(1, HEADERS.length);
}

function doGet() {
  return json_({ ok: true, service: 'ABM Zoom form', time: new Date().toISOString() });
}

function doPost(e) {
  var p = (e && e.parameter) || {};
  try {
    if (p.website) return json_({ ok: true });                       // honeypot: bot
    var name = clean_(p.name, 80), phone = clean_(p.phone, 20), email = clean_(p.email, 120);
    if (name.length < 2) return json_({ ok: false, error: 'Vui lòng nhập họ và tên.' });
    if (!/^\+?\d{9,15}$/.test(phone)) return json_({ ok: false, error: 'Số điện thoại chưa hợp lệ.' });
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email)) return json_({ ok: false, error: 'Email chưa hợp lệ.' });

    var id = clean_(p.submission_id, 40) || Utilities.getUuid();
    var cache = CacheService.getScriptCache();
    if (cache.get('sub_' + id)) return json_({ ok: true, duplicate: true }); // chống gửi trùng

    var lock = LockService.getScriptLock();
    lock.waitLock(20000);
    try {
      getSheet_().appendRow([
        Utilities.formatDate(new Date(), 'Asia/Ho_Chi_Minh', 'yyyy-MM-dd HH:mm:ss'),
        safe_(name), "'" + phone, safe_(email), safe_(clean_(p.role, 60)), safe_(clean_(p.sessions, 80)),
        safe_(clean_(p.need, 500)), safe_(clean_(p.consent, 10)),
        safe_(clean_(p.utm_source, 80)), safe_(clean_(p.utm_medium, 80)), safe_(clean_(p.utm_campaign, 120)),
        safe_(clean_(p.page, 300)), "'" + id, 'Mới', ''
      ]);
      cache.put('sub_' + id, '1', 21600);
    } finally {
      lock.releaseLock();
    }

    if (NOTIFY_EMAIL) {
      MailApp.sendEmail(NOTIFY_EMAIL, '[ABM Zoom] Đăng ký mới: ' + name,
        'Họ tên: ' + name + '\nSĐT: ' + phone + '\nEmail: ' + email +
        '\nVai trò: ' + (p.role || '') + '\nBuổi: ' + (p.sessions || '') + '\nNhu cầu: ' + (p.need || ''));
    }
    return json_({ ok: true, id: id });
  } catch (err) {
    console.error(err);
    return json_({ ok: false, error: 'Hệ thống đang bận. Vui lòng thử lại.' });
  }
}

function clean_(v, max) { return String(v == null ? '' : v).replace(/[\u0000-\u001F]/g, ' ').trim().slice(0, max); }
// Chặn chèn công thức vào Sheet (=, +, -, @ ở đầu chuỗi).
function safe_(v) { return /^[=+\-@]/.test(v) ? "'" + v : v; }
function json_(o) { return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON); }

/** Test nhanh trong trình soạn Apps Script (Chạy → testPost) — ghi 1 dòng TEST vào Sheet. */
function testPost() {
  var r = doPost({ parameter: { name: 'TEST - xóa dòng này', phone: '0900000000', email: 'test@example.com',
    role: 'Khác', sessions: 'Buổi 01 - 30/09', consent: 'Có', submission_id: 'TEST' + Date.now() } });
  Logger.log(r.getContent());
}
