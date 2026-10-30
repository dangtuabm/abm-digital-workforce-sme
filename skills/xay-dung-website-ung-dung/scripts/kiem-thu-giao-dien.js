// KIỂM THỬ GIAO DIỆN NHIỀU TRANG, NHIỀU KHỔ MÀN HÌNH
// Chạy trong trình duyệt (bảng điều khiển DevTools) khi đang mở site trên máy hoặc bản xem trước, cùng tên miền với các trang cần kiểm.
// Cách dùng:
//   1. Dán toàn bộ file này vào bảng điều khiển (Console) rồi Enter.
//   2. Gọi: const ketQua = await window.__kiemThuGiaoDien(['/', '/gioi-thieu', '/lien-he'], [1440, 375, 320]);
//   3. console.table(ketQua)
// Tham số thứ ba (tùy chọn): bộ chọn CSS của các vùng được bỏ qua (dải chữ chạy, băng chuyền cuộn ngang có chủ ý).
//   Mặc định: '[data-bo-qua-kiem-thu]' — gắn thuộc tính này vào vùng cần bỏ qua.
// Các loại lỗi trả về:
//   TRAN  — trang tràn ngang (có thanh cuộn ngang) ở khổ màn hình đó
//   HEP   — chữ bị ép vào cột hẹp dưới 90px, đọc không được
//   MOCOI — chữ cuối đoạn rơi lẻ một mình xuống dòng riêng
//   DAU   — dòng mở đầu bằng dấu — · & | (ngắt dòng xấu)
window.__kiemThuGiaoDien = async (trang, kho = [1440, 375, 320], boQua = '[data-bo-qua-kiem-thu]') => {
  const ketQua = [];
  const layTu = (doc, el) => {
    const ds = [];
    const tw = doc.createTreeWalker(el, NodeFilter.SHOW_TEXT);
    let n;
    while ((n = tw.nextNode())) {
      const re = /[^ \t\r\n]+/g; let m;
      while ((m = re.exec(n.data))) ds.push([n, m.index, m.index + m[0].length, m[0]]);
    }
    return ds;
  };
  const khung = (doc, t) => { const r = doc.createRange(); r.setStart(t[0], t[1]); r.setEnd(t[0], t[2]); return r.getClientRects()[0]; };
  for (const w of kho) {
    for (const duongDan of trang) {
      const f = document.createElement('iframe');
      f.style.cssText = `position:fixed;left:-${w + 50}px;top:0;width:${w}px;height:900px;border:0`;
      document.body.appendChild(f);
      await new Promise((res) => { f.onload = res; f.src = duongDan; setTimeout(res, 15000); });
      await new Promise((res) => setTimeout(res, 600));
      const d = f.contentDocument, win = f.contentWindow;
      if (!d) { ketQua.push({ kho: w, trang: duongDan, loi: 'KHONG_MO_DUOC', chi_tiet: 'Trang khác tên miền hoặc mở bằng file:// — chạy qua máy chủ thử trên máy' }); f.remove(); continue; }
      try { await d.fonts.ready; } catch { /* bỏ qua */ }
      // 1. Tràn ngang
      if (d.documentElement.scrollWidth > w + 2) {
        const thuPham = [];
        for (const el of d.body.querySelectorAll('*')) {
          const r = el.getBoundingClientRect();
          if (r.right > w + 2 && r.width > 0 && r.width < 3000 && win.getComputedStyle(el).position !== 'fixed'
            && !el.closest(boQua)) thuPham.push(`${el.tagName}.${String(el.className).split(' ')[0]}`);
        }
        ketQua.push({ kho: w, trang: duongDan, loi: 'TRAN', chi_tiet: `rộng ${d.documentElement.scrollWidth}px :: ${thuPham.slice(0, 3).join(' | ')}` });
      }
      const daGap = new Set();
      for (const el of d.querySelectorAll('h1,h2,h3,h4,p,li,dt,dd,figcaption,blockquote,a,button,span,b,strong,label')) {
        if (el.closest(`[hidden],[aria-hidden="true"],svg,${boQua}`)) continue;
        if ([...el.children].some((c) => c.matches('p,li,h1,h2,h3,h4,div,ul,ol'))) continue;
        const cs = win.getComputedStyle(el);
        if (cs.display === 'none' || cs.visibility === 'hidden') continue;
        const chu = (el.textContent || '').replace(/\s+/g, ' ').trim();
        if (chu.length < 12 || daGap.has(chu)) continue;
        // 2. Chữ bị ép cột hẹp
        const rg = d.createRange(); rg.selectNodeContents(el);
        const rs = [...rg.getClientRects()].filter((r) => r.width > 0);
        if (chu.length >= 25 && rs.length >= 3 && Math.max(...rs.map((r) => r.width)) < 90) { daGap.add(chu); ketQua.push({ kho: w, trang: duongDan, loi: 'HEP', chi_tiet: `${el.tagName} :: ${chu.slice(0, 50)}` }); continue; }
        const lh = parseFloat(cs.lineHeight) || parseFloat(cs.fontSize) * 1.3;
        if (el.getBoundingClientRect().height < lh * 1.6) continue;
        const tu = layTu(d, el);
        if (tu.length < 3) continue;
        const khoi = (nd) => { let e = nd.parentElement; while (e && e !== el && win.getComputedStyle(e).display.startsWith('inline')) e = e.parentElement; return e; };
        const cuoi = tu[tu.length - 1], truoc = tu[tu.length - 2];
        if (khoi(cuoi[0]) === khoi(truoc[0])) {
          const a = khung(d, truoc), b = khung(d, cuoi);
          // 3. Chữ cuối rơi xuống dòng riêng
          if (a && b && b.top - a.top > lh * 0.5 && !/ /.test(cuoi[3]) && cuoi[3].length <= 8) { daGap.add(chu); ketQua.push({ kho: w, trang: duongDan, loi: 'MOCOI', chi_tiet: `[${cuoi[3]}] :: ${chu.slice(-70)}` }); continue; }
        }
        // 4. Dòng mở đầu bằng dấu
        for (let i = 1; i < tu.length; i++) {
          if (/^[—–·|&]$/.test(tu[i][3])) {
            const p = khung(d, tu[i - 1]), q = khung(d, tu[i]);
            if (p && q && q.top - p.top > lh * 0.5) { daGap.add(chu); ketQua.push({ kho: w, trang: duongDan, loi: 'DAU', chi_tiet: `[${tu[i][3]}] :: ${chu.slice(0, 70)}` }); break; }
          }
        }
      }
      f.remove();
    }
  }
  return ketQua;
};
