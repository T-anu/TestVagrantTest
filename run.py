class Shopping:
    
    def gst():
        
        
        Shopping_Cart=[["Leather wallet",1100,18,1],
               ["Umbrella",900,12,4],
               ["Cigarette",200,28,3],
               ["Honey",100,0,2]]
        gst_money=[]
        for i in range(0,len(Shopping_Cart)):
            for j in range(1,len(Shopping_Cart)):
                gst_amount=int((Shopping_Cart[i][2]/100)*Shopping_Cart[i][1])
                number_of_items=gst_amount*Shopping_Cart[i][3]
                gst_money.append(number_of_items)
          
        print('Maximum gst to be paid :',max(gst_money), Shopping_Cart[1][0])
        
        
    def total_amount():
        
        
        Shopping_Cart=[["Leather wallet",1100,18,1],
               ["Umbrella",900,12,4],
               ["Cigarette",200,28,3],
               ["Honey",100,0,2]]
        Total=[]
        
        for i in range(0,len(Shopping_Cart)):
            for j in range(1,len(Shopping_Cart)):
                gst_amount=int((Shopping_Cart[i][2]/100)*Shopping_Cart[i][1])
                Sub_Total=(gst_amount*Shopping_Cart[i][3])
                Total_1=Sub_Total+(Shopping_Cart[i][1]*Shopping_Cart[i][3])
            Total.append(Total_1)
        
        sum=0
        for i in range(len(Total)):
            sum=Total[i]+sum
        print('Total amount :',sum)
                
                
S=Shopping
S.gst()
S.total_amount()
    
        


            
