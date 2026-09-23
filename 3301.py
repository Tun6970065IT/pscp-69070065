"""box"""

def box():
    """box"""
    w , l , m ,n = map(int , input().split())
    ans = w * l
    for i in range(m , n+1):
        use = (l // i * i * w) + (l % i * (w // i) * i)
        #(จำนวนชิ้นที่ใส่ได้ใน1แถว * ความยาวสินค้า * กว้าง)
        # +
        #(เศษท้ายกล่อง * สินค้าที่ใส่ได้1แถวตามตวามกว้าง * ยาวสินค้า)
        not_use = (w * l) - use # หาพื้นที่ว่าง
        if not_use < ans:
            ans = not_use #จำนวนพื้นที่ว่างน้อยกว่าพื้นที่กล่องทั้งหมด
    print(ans)
box()
