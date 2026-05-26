"""
Input:
choice_input: Chuỗi lựa chọn menu
input_shop, input_product, input_desc, input_category, input_keywords: Thông tin sản phẩm mà ta sẽ nhập vào
new_voucher: Mã giảm giá cần kiểm tra ở chức năng 3
search_keyword, replace_keyword: Từ khóa tìm kiếm và thay thế ở chức năng 4
Output: Báo cáo thống kê sản phẩm, tên shop chuẩn hóa, thông báo trạng thái mã giảm giá, mô tả sản phẩm sau khi chỉnh sửa

Luồng chương trình:
Bước 1: Sử dụng vòng lặp while hiển thị menu. Nhập choice_input, kiểm tra hợp lệ trước khi ép kiểu sang số nguyên choice
Bước 2: Phân nhánh xử lý bằng match choice
Case 1: Nhập thông tin sản phẩm. Kiểm tra rỗng cho tên shop và mô tả.  Tách chuỗi từ khóa rồi in báo cáo thống kê 
Case 2: Kiểm tra dữ liệu tồn tại hay ko. Chuẩn hóa tên shop bằng cách loại bỏ khoảng trắng, 
chuyển chữ thường, thay khoảng trắng bằng dấu gạch ngang rồi kiểm tra và thêm tiền tố "shop-" nếu chưa có
Case 3: Kiểm tra dữ liệu tồn tại hay ko. Nhập new_voucher và lọc qua 6 điều kiện như 
(rỗng, chứa khoảng trắng, độ dài từ 6 đến 12, viết hoa toàn bộ, chỉ chứa chữ và số, bắt đầu bằng SALE) 
Nếu hợp lệ thì thêm vào danh sách mã giảm giá.
Case 4: Kiểm tra dữ liệu tồn tại hay ko. Nhận từ khóa tìm kiếm và thay thế 
Dùng toán tử in để kiểm tra rồi để đếm số lần xuất hiện và cập nhật mô tả mới.
Case 5: In thông báo và dùng lệnh break để thoát vòng lặp.
Case _: Báo lỗi trực tiếp nếu người dùng nhập số nằm ngoài khoảng từ 1 đến 5.
"""

shop_name = ""
product_name = ""
product_description = ""
product_category = ""
keyword_list = []
voucher_list = []

while True:
    print("""
+==================================================================+
|             HỆ THỐNG QUẢN LÝ NỘI DUNG SẢN PHẨM SHOPPEE           |
+==================================================================+
|   1. Nhập dữ liệu sản phẩm và xem báo cáo thống kê               |
|   2. Chuẩn hóa tên shop                                          |
|   3. Kiểm tra mã giảm giá hợp lệ                                 |
|   4. Tìm kiếm và thay thế từ khóa trong mô tả sản phẩm           |
|   5. Thoát chương trình                                          |
+==================================================================+
""")
    
    choice_input = input("> Mời bạn chọn chức năng (1-5): ").strip()
    
    if not choice_input.isdigit():
        print("Lựa chọn không hợp lệ! Vui lòng nhập một số nguyên từ 1 đến 5.")
        continue
        
    choice = int(choice_input)
    
    match choice:
        case 1:
            input_shop = input("Nhập tên shop: ")
            if input_shop.strip() == "":
                print("Lỗi: Tên shop không được bỏ trống!")
                continue
                
            input_product = input("Nhập tên sản phẩm: ")
            
            input_desc = input("Nhập mô tả sản phẩm: ")
            if input_desc.strip() == "":
                print("Lỗi: Mô tả sản phẩm không được rỗng!")
                continue
                
            input_category = input("Nhập danh mục sản phẩm: ")
            input_keywords = input("Nhập danh sách từ khóa tìm kiếm (cách nhau bởi dấu phẩy): ")
            
            shop_name = input_shop
            product_name = input_product
            product_description = input_desc
            product_category = input_category
            
            keyword_list = []
            raw_keywords = input_keywords.split(",")
            for keyword in raw_keywords:
                clean_keyword = keyword.strip()
                if clean_keyword != "":
                    keyword_list.append(clean_keyword)
                    
            print("\n--- BÁO CÁO THỐNG KÊ SẢN PHẨM ---")
            print("Tên shop (đã strip):", shop_name.strip())
            print("Tên sản phẩm (chuẩn hóa chữ đầu):", product_name.strip().title())
            print("Mô tả sản phẩm (đã strip):", product_description.strip())
            print("Độ dài mô tả sản phẩm:", len(product_description))
            print("Danh mục sản phẩm (chuẩn hóa):", product_category.strip().lower())
            print("Danh sách từ khóa:", keyword_list)
            print("Số lượng từ khóa tìm kiếm:", len(keyword_list))
            print("Mô tả sản phẩm chữ thường:", product_description.lower())
            print("Mô tả sản phẩm chữ hoa:", product_description.upper())

        case 2:
            if shop_name == "":
                print("Vui lòng chạy Chức năng 1 để nhập tên shop trước!")
                continue
                
            shop_clean = shop_name.strip().lower()
            shop_hyphen = shop_clean.replace(" ", "-")
            
            if not shop_hyphen.startswith("shop-"):
                normalized_shop = "shop-" + shop_hyphen
            else:
                normalized_shop = shop_hyphen
                
            print("\n--- KẾT QUẢ CHUẨN HÓA TÊN SHOP ---")
            print("Tên shop ban đầu:", shop_name)
            print("Tên shop sau khi được chuẩn hóa:", normalized_shop)

        case 3:
            if shop_name == "":
                print("Vui lòng chạy Chức năng 1 để khởi tạo dữ liệu trước!")
                continue
                
            new_voucher = input("Nhập mã giảm giá cần kiểm tra: ")
            
            if new_voucher == "":
                print("Lỗi: Mã giảm giá không được rỗng!")
                continue
                
            if " " in new_voucher:
                print("Lỗi: Mã giảm giá không được chứa khoảng trắng!")
                continue
                
            if len(new_voucher) < 6 or len(new_voucher) > 12:
                print("Lỗi: Mã giảm giá phải có độ dài từ 6 đến 12 ký tự!")
                continue
                
            if new_voucher != new_voucher.upper():
                print("Lỗi: Mã giảm giá phải được viết hoa toàn bộ!")
                continue
                
            if not new_voucher.isalnum():
                print("Lỗi: Mã giảm giá chỉ được chứa chữ cái và chữ số!")
                continue
                
            if not new_voucher.startswith("SALE"):
                print("Lỗi: Mã giảm giá phải bắt đầu bằng chuỗi SALE!")
                continue
                
            print("Mã giảm giá hợp lệ!")
            voucher_list.append(new_voucher)
            print("Danh sách mã giảm giá hiện tại:", voucher_list)

        case 4:
            if product_description == "":
                print("Vui lòng chạy Chức năng 1 để nhập mô tả trước!")
                continue
                
            search_keyword = input("Nhập từ khóa cần tìm: ").strip()
            replace_keyword = input("Nhập từ khóa thay thế: ").strip()
            
            if search_keyword in product_description:
                count_appearances = product_description.count(search_keyword)
                updated_description = product_description.replace(search_keyword, replace_keyword)
                product_description = updated_description
                
                print("\n--- KẾT QUẢ TÌM KIẾM & THAY THẾ ---")
                print("Số lần xuất hiện của từ khóa:", count_appearances)
                print("Mô tả sau khi thay thế:", product_description)
            else:
                print(f"Không tìm thấy từ khóa '{search_keyword}' trong mô tả sản phẩm.")

        case 5:
            print("Thoát chương trình!")
            break

        case _:
            print("Lựa chọn không hợp lệ! Vui lòng chọn lại trong khoảng từ 1 đến 5.")
