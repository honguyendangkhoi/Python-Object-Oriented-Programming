print("Blind bids")
bids=[]
over=True
winner_bid = 0
winner_name = ""
while over==True:
    name=input("what's your name: ")
    price=float(input("what's your bid: "))
    choice=input("if there are anyone else want to bid?: ")
    bids_new={
        "name":name,
        "bid":price,
    }
    bids.append(bids_new)
    if choice == 'yes':
        print("\n"*100)
    elif choice=='no':
        for bid_win in bids:
            if bid_win['bid'] > winner_bid:
                winner_bid=bid_win['bid']
                winner_name=bid_win['name']
        print(f"you won:{winner_name} - bid: {winner_bid}")
        over=False
    else:
        print("invalid")

#note loi sai:
# 1 dấu '=' là gán giá trị, 2 dấu là so sánh

# tạo dict {"bid":price} thì tất cả đều phải dùng bid, vì trong dấu ""
# nên bid là key, còn price là value 

#phải nhớ có int, float(input)

#swap thì phải thằng nhỏ hơn cho thằng lớn hơn, sau cho trước

#nếu tạo 1 list riêng để chứa dict thì nên để nó ngoài những vòng điều kiện
#để khi nhập xong nó tự lưu vào

#để thêm, xóa hay so sánh gì từ dict thì phải tạo thêm 1 list để chứa nó
#rồi lấy từ list đó ra để làm, không đụng vô dict nữa

#nếu muốn so sánh để print ra min, max thì nên tạo thêm biến riêng cho nó
#để so sánh
