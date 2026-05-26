"""
Input:
choice_input: Chuỗi lựa chọn menu
input_user, input_title, input_desc, input_hashtags: Thông tin của video mà ta sẽ nhập vào
new_hashtag: dùng ở chức năng 3
search_keyword, replace_keyword: Từ khóa tìm kiếm và thay thế ở chức năng 4
Output: Báo cáo thống kê video, tên tài khoản chuẩn hóa, thông báo trạng thái hashtag, mô tả video sau khi chỉnh sửa

Luồng chương trình:
Bước 1: Sử dụng vòng lặp vô hạn while hiển thị menu  
Nhập choice_input, kiểm tra hợp lệ trước khi ép kiểu sang số nguyên choice
Bước 2: Phân nhánh xử lý bằng match choice
Case 1: Nhận các thông tin của video. Kiểm tra rỗng cho tài khoản và mô tả  
Tách chuỗi hashtag rồi in báo cáo thống kê và tính số từ
Case 2: Kiểm tra dữ liệu có tồn tại ko. Chuẩn hóa tài khoản bằng cách loại bỏ khoảng trắng thừa, chuyển chữ thường và thêm ký tự @ ở đầu
Case 3: Kiểm tra dữ liệu tồn tại có tồn tại ko. Nhận new_hashtag và lọc qua các điều kiện như 
(rỗng, bắt đầu bằng #, chứa khoảng trắng, độ dài tối thiểu, ký tự chữ số hoặc dấu gạch dưới). 
Nếu hợp lệ thêm vào danh sách.
Case 4: Kiểm tra dữ liệu có tồn tại ko. Nhập từ khóa tìm kiếm và thay thế. Dùng toán tử in để kiểm tra, 
rồi đếm số lần xuất hiện và rồi cập nhật mô tả mới.
Case 5: In thông báo và dùng lệnh break để thoát vòng lặp.
Case _: Báo lỗi trực tiếp nếu người dùng nhập số nằm ngoài khoảng từ 1 đến 5.
"""

username = ""
video_title = ""
video_description = ""
hashtag_list = []

while True:
    print("""
+==============================================================+
|             HỆ THỐNG QUẢN LÝ NỘI DUNG TIKTOK                 |
+==============================================================+
|   1. Nhập và phân tích thông tin video                       |
|   2. Chuẩn hóa tên tài khoản                                 |
|   3. Kiểm tra tính hợp lệ của hashtag                        |
|   4. Tìm kiếm và thay thế từ khóa trong mô tả                |
|   5. Thoát chương trình                                      |
+==============================================================+
""")
    
    choice_input = input("> Mời bạn chọn chức năng (1-5): ").strip()
    
    if not choice_input.isdigit():
        print("Lựa chọn không hợp lệ! Vui lòng nhập một số nguyên từ 1 đến 5.")
        continue
        
    choice = int(choice_input)
    
    match choice:
        case 1:
            input_user = input("Nhập tên tài khoản người đăng: ")
            if input_user.strip() == "":
                print("Lỗi: Tên tài khoản không được rỗng!")
                continue
                
            input_title = input("Nhập tiêu đề video: ")
            
            input_desc = input("Nhập mô tả video: ")
            if input_desc.strip() == "":
                print("Lỗi: Mô tả video không được rỗng!")
                continue
                
            input_hashtags = input("Nhập danh sách hashtag (cách nhau bởi dấu phẩy): ")
            
            username = input_user
            video_title = input_title
            video_description = input_desc
            
            hashtag_list = []
            raw_hashtags = input_hashtags.split(",")
            for tag in raw_hashtags:
                clean_tag = tag.strip()
                if clean_tag != "":
                    hashtag_list.append(clean_tag)
                    
            print("\n--- BÁO CÁO THỐNG KÊ VIDEO ---")
            print("Tên tài khoản (đã strip):", username.strip())
            print("Tiêu đề (chuẩn hóa chữ đầu):", video_title.strip().title())
            print("Mô tả (đã strip):", video_description.strip())
            print("Độ dài mô tả video:", len(video_description))
            print("Số lượng từ trong mô tả:", len(video_description.split()))
            print("Danh sách hashtag:", hashtag_list)
            print("Số lượng hashtag:", len(hashtag_list))
            print("Mô tả dạng chữ thường:", video_description.lower())
            print("Mô tả dạng chữ hoa:", video_description.upper())

        case 2:
            if username == "":
                print("Vui lòng chạy Chức năng 1 để nhập tên tài khoản trước!")
                continue
                
            clean_username = username.strip().lower()
            normalized_username = "@" + clean_username
            
            print("\n--- KẾT QUẢ CHUẨN HÓA TÊN TÀI KHOẢN ---")
            print("Tên tài khoản ban đầu:", username)
            print("Tên tài khoản sau khi chuẩn hoá:", normalized_username)

        case 3:
            if username == "":
                print("Vui lòng chạy Chức năng 1 để khởi tạo dữ liệu video trước!")
                continue
                
            new_hashtag = input("Nhập một hashtag cần kiểm tra: ")
            
            if new_hashtag == "":
                print("Lỗi: Hashtag không được rỗng!")
                continue
                
            if not new_hashtag.startswith("#"):
                print("Lỗi: Hashtag phải bắt đầu bằng ký tự #!")
                continue
                
            if " " in new_hashtag:
                print("Lỗi: Hashtag không được chứa khoảng trắng!")
                continue
                
            if len(new_hashtag) < 2:
                print("Lỗi: Hashtag phải có ít nhất 2 ký tự, bao gồm cả ký tự #!")
                continue
                
            content_after_hash = new_hashtag[1:]
            is_valid_chars = True
            for char in content_after_hash:
                if not (char.isalnum() or char == "_"):
                    is_valid_chars = False
                    break
                    
            if not is_valid_chars:
                print("Lỗi: Hashtag chỉ nên sử dụng chữ cái, chữ số hoặc dấu gạch dưới sau ký tự #!")
                continue
                
            print("Hashtag hợp lệ!")
            hashtag_list.append(new_hashtag)
            print("Đã thêm thành công. Danh sách hashtag hiện tại:", hashtag_list)

        case 4:
            if video_description == "":
                print("Vui lòng chạy Chức năng 1 để nhập mô tả video trước!")
                continue
                
            search_keyword = input("Nhập từ khóa cần tìm: ").strip()
            replace_keyword = input("Nhập từ khóa thay thế: ").strip()
            
            if search_keyword in video_description:
                count_appearances = video_description.count(search_keyword)
                video_description = video_description.replace(search_keyword, replace_keyword)
                
                print("\n--- KẾT QUẢ TÌM KIẾM & THAY THẾ ---")
                print("Tìm thấy từ khóa!")
                print("Số lần từ khóa xuất hiện trong mô tả:", count_appearances)
                print("Mô tả video sau khi thay thế:", video_description)
            else:
                print(f"Không tìm thấy từ khóa '{search_keyword}' trong mô tả video.")

        case 5:
            print("Thoát chương trình!")
            break

        case _:
            print("Lựa chọn không hợp lệ! Vui lòng chọn lại trong khoảng từ 1 đến 5.")
