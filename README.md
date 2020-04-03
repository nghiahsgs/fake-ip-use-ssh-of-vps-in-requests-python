# fake-ip-use-ssh-of-vps-in-requests-python
fake ip use ssh of vps in requests python

## Hướng dẫn các bước để fake ip cho tool python
Các fake ip này áp dụng cho tool python dùng thư viện requests, vd khi bạn làm tool auto search youtube một keyword, nếu bạn thực hiện thao tác search liên tục cùng 1 ip, bạn sẽ bạn chặn. Giải pháp đặt ra là bạn cần fake ip và fake ip qua ssh là một cách đó.

## ssh là gì
ssh là một giao thức để kết nối từ client đến máy chủ từ xa. Có 2 loại kết nối ssh, một là chỉ cần user và pass là kết nối được. Cách 2 bảo mật hơn là dùng ssh key. Nói về cách thứ 2, ở máy chủ cần có một public key, máy mình (client) cần một private key, khi 2 key này khớp với nhau theo một hình thức mã hóa thì bạn có thể kết nói thành công. Đó là nói qua về cách thứ 2. Ở đây tôi chỉ dùng cách 1: user và pass để kết nối ssh tới server.

## B1: Mua vps
Như vậy cầm có ssh đã : đi mua vps. Mua đâu cũng được, miễn là có một user, pass và ip của máy chủ

## B2: Dùng phần mềm bitvise ssh client 
Dùng phần mềm này để kết nois với server, ở tab service, nó một mục là sock. Listen interface các bạn để nguyên là localhost (hoặc 127.0.0.1) và port là cổng tùy thích, thường thì mặc định là 1080.

### Đến đây bạn đã có được sock ip và sock port
### Lưu ý 
bạn có thể bỏ qua bước một và bước 2 bằng cách đi mua trực tiếp sock, một sống trang bán như vietpn sao ý, nc cái này đi gõ google hoặc fb nhiều người bán lắm. Khi mua sock, họ sẽ cho bạn sock ip, port và user và pass của sock đó

## B3: Dùng nó và thư viện requests
Đọc code mình có code mẫu cách dùng sock trong thư viện requests.Good luck

## bonus
Khi muốn chuyển nhiều ip liên tục, mở nhiều tab bitvise client lên, mỗi cái kết nối một ip và forward đến một port riêng biệt của local host (ex : 1080, 1081 ...) Sau đó.Trong code chỉ cần thay port đi là ip đã được fake

### Happy coding