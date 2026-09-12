# LOCALIZATION CONTRACT RULES

## Locale không chỉ là ngôn ngữ

Dùng mã language–script–region khi cần, ví dụ `en-US`, `vi-VN`, `zh-Hant-TW`. Cùng ngôn ngữ nhưng khác thị trường có thể khác xưng hô, chính tả, tiền tệ, ngày, pháp lý và cultural fit.

## Freedom level

- `LITERAL`: giữ meaning/cấu trúc gần source; dùng cho legal, technical, safety khi contract yêu cầu.
- `ADAPTIVE`: ưu tiên tự nhiên và chức năng trong cùng claim/intent.
- `TRANSCREATION`: đổi cách biểu đạt theo creative brief; không đổi factual claim, offer boundary hoặc legal meaning.

## Thuật ngữ

Mỗi term có source term, target term, status `APPROVED / PREFERRED / FORBIDDEN / CANDIDATE`, domain, case/plural rule, example, owner và version. `CANDIDATE` không được dùng như approved trong high-risk release.

## Locale conversion

- Date/time: giữ raw; chỉ normalize khi source format/timezone rõ.
- Currency/unit: format ký hiệu theo locale nhưng chỉ quy đổi value khi contract có rate, source, date và rounding.
- Number: giữ magnitude, sign, denominator và precision; cảnh giác dấu phẩy/chấm.
- Name/address/phone: transliterate/format theo rule; không dịch tên riêng tùy ý.
- Example/culture: chỉ thay khi creative/localization brief cho phép và meaning tương đương được reviewer duyệt.

## Locked technical content

Placeholder, variable, ICU plural key, HTML/XML tag, Markdown link target, code, file path và product/framework name phải giữ parity theo contract. Target được đổi visible link text nhưng không tự đổi URL.

