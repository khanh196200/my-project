nhập  pygame , sys , ngẫu nhiên
từ  pygame . nhập khẩu địa phương  * 

WINDOWWIDTH  =  600
Cửa sổ  =  150
FPS  =  60


CẤP  =  0,75

TỐC ĐỘ_GROUND  =  6
IMG_GROUND  =  pygame . hình ảnh . tải ( 'img / ground.png' )

TỐC ĐỘ_KY  =  1
IMG_SKY  =  pygame . hình ảnh . tải ( 'img / sky.png' )

IMG_TREX  =  pygame . hình ảnh . tải ( 'img / tRex.png' )
TIME_CHANGE_TREX  =  6
Y_TREX  =  105
X_TREX  =  50
CAO_MIN  =  90
TỐC ĐỘ_REX  =  - 12,5

IMG_CATUS  =  pygame . hình ảnh . tải ( 'img / cactus.png' )
Y_CATUS  =  100

BIRD_IMG  =  pygame . hình ảnh . tải ( 'img / bird.png' )
TIME_CHANGE_BIRD  =  10
Y_BIRD_1  =  110
Y_BIRD_2  =  80
Y_BIRD_3  =  50

DISTANCE_MIN  =  400
DISTANCE_MAX  =  600


trăn . init ()
trăn . hiển thị . set_caption ( 'T-REX' )
FPSCLOCK  =  pygame . thời gian . Đồng hồ ()
HIỂN THỊ  =  pygame . hiển thị . set_mode (( WINDOWWIDTH , WINDOWHEIGHT ))

lớp  T_Rex ():
    def  __init__ ( tự , tùy chọn  =  3 ):
        tự . x  =  X_TREX
        tự . y  =  Y_TREX
        tự . tốc độ  =  0
        tự . img  =  IMG_TREX
        tự . tùy chọn  =  tùy chọn
        tự . bề mặt  =  pygame . Bề mặt (( 55 , 43 ), pygame . SRCALPHA )
        tự . bề mặt . blit ( tự . img , ( 0 , 0 ), ( 80 , 0 , 40 , 43 ))
        tự . Thời gian thay đổi  =  0
        tự . nhảy  =  sai
        tự . hạ thấp  =  Sai
    
     cập nhật def ( tự , lên , xuống ):
        tự . bề mặt . điền (( 0 , 0 , 0 , 0 ))
        nếu  không  tự . nhảy :
            nếu  lên :
                tự . nhảy  =  đúng
                tự . tốc độ  =  SPEED_TREX
            elif  xuống :
                tự . hạ thấp  =  Đúng
                nếu  tự . Thay đổi thời gian  <=  TIME_CHANGE_TREX :
                    tự . tùy chọn  =  4
                khác :
                    tự . tùy chọn  =  5
                tự . Thời gian thay đổi  + =  1
                nếu  tự . Thay đổi thời gian  >  TIME_CHANGE_TREX  *  2 :
                    tự . Thời gian thay đổi  =  0
                
            khác :
                nếu  tự . Thay đổi thời gian  <=  TIME_CHANGE_TREX :
                    tự . tùy chọn  =  0
                khác :
                    tự . tùy chọn  =  1
                tự . Thời gian thay đổi  + =  1
                nếu  tự . Thay đổi thời gian  >  TIME_CHANGE_TREX  *  2 :
                    tự . Thời gian thay đổi  =  0
        elif  tự . nhảy :
            tự . tùy chọn  =  2

            nếu  tự . y  <=  Y_TREX  -  HIGH_MIN  và  tự . tốc độ  <  0  và ( không  lên ):
                tự . tốc độ  =  0
            tự . y  + =  int ( tự . tốc độ  +  GRAVITY / 2 )
            tự . tốc độ  + =  GRAVITY

            nếu  tự . y  > =  Y_TREX :
                tự . nhảy  =  sai
                tự . y  =  Y_TREX

                
        nếu  tự . tùy chọn  ==  0 :
            tự . bề mặt . blit ( tự . img , ( 0 , 0 ), ( 0 , 0 , 40 , 43 ))
        elif  tự . tùy chọn  ==  1 :
            tự . bề mặt . blit ( tự . img , ( 0 , 0 ), ( 40 , 0 , 40 , 43 ))
        elif  tự . tùy chọn  ==  2 :
            tự . bề mặt . blit ( tự . img , ( 0 , 0 ), ( 80 , 0 , 40 , 43 ))
        elif  tự . tùy chọn  ==  3 :
            tự . bề mặt . blit ( tự . img , ( 0 , 0 ), ( 120 , 0 , 40 , 43 ))
        elif  tự . tùy chọn  ==  4 :
            tự . bề mặt . blit ( tự . img , ( 0 , 0 ), ( 160 , 0 , 55 , 43 ))
        elif  tự . tùy chọn  ==  5 :
            tự . bề mặt . blit ( tự . img , ( 0 , 0 ), ( 215 , 0 , 55 , 43 ))
        
    
    def  vẽ ( tự ):
        HIỂN THỊ . blit ( tự . bề mặt , ( tự . x , tự . y ))

lớp  Catus ():
    def  __init__ ( tự , x , y , tùy chọn ):
        tự . x  =  x
        tự . y  =  y
        tự . tùy chọn  =  tùy chọn
        tự . img  =  IMG_CATUS
        tự . trực tràng  = [ 0 , 0 , 0 , 0 ]
        nếu  tùy chọn  ==  0 :
            tự . trực tràng  = [ 0 , 0 , 23 , 46 ]
         tùy chọn  elif ==  1 :
            tự . trực tràng  = [ 0 , 0 , 47 , 46 ]
         tùy chọn  elif ==  2 :
            tự . trực tràng  = [ 100 , 0 , 49 , 46 ]
         tùy chọn  elif ==  3 :
            tự . trực tràng  = [ 100 , 0 , 49 , 46 ]
         tùy chọn  elif ==  4 :
            tự . trực tràng  = [ 25 , 0 , 73 , 46 ]
        tự . bề mặt  =  pygame . Surface (( tự . Rect [ 2 ], tự . Rect [ 3 ]), pygame . SRCALPHA )
        tự . bề mặt . blit ( tự . img , ( 0 , 0 ), tự . rect )

    
     cập nhật def ( tự , tốc độ ):
        tự . x  - =  int ( tốc độ )
    
    def  vẽ ( tự ):
        HIỂN THỊ . blit ( tự . bề mặt , ( tự . x , tự . y ))


lớp  Chim ():
    def  __init__ ( tự , x , y , tùy chọn  =  0 ):
        tự . x  =  x
        tự . y  =  y
        tự . tùy chọn  =  tùy chọn
        tự . bề mặt  =  pygame . Bề mặt (( 42 , 36 ), pygame . SRCALPHA )
        tự . Thời gian thay đổi  =  0
        tự . img  =  pygame . hình ảnh . tải ( 'img / bird.png' )
    
     cập nhật def ( tự , tốc độ ):
        tự . bề mặt . điền (( 0 , 0 , 0 , 0 ))

        tự . x  - =  int ( tốc độ )

        nếu  tự . Thay đổi thời gian  <=  TIME_CHANGE_BIRD :
            tự . tùy chọn  =  0
        khác :
            tự . tùy chọn  =  1
        tự . Thời gian thay đổi  + =  1
        nếu  tự . Thời gian Thay đổi  >  TIME_CHANGE_BIRD  *  2 :
            tự . Thời gian thay đổi  =  0
        
        nếu  tự . tùy chọn  ==  0 :
            tự . bề mặt . blit ( tự . img , ( 0 , 0 ), ( 0 , 0 , 42 , 36 ))
        elif  tự . tùy chọn  ==  1 :
            tự . bề mặt . blit ( tự . img , ( 0 , 0 ), ( 42 , 0 , 42 , 36 ))
    
    def  vẽ ( tự ):
        HIỂN THỊ . blit ( tự . bề mặt , ( tự . x , tự . y ))



lớp  ListCatusAndBirds ():
    def  __init__ ( tự ):
        tự . danh sách  = []
        cho  i  trong  phạm vi ( 0 , 3 ):
            tự . danh sách . chắp thêm ( Catus ( 500  +  WINDOWWIDTH  +  ngẫu nhiên . randint ( DISTANCE_MIN , DISTANCE_MAX ) * i , Y_CATUS , ngẫu nhiên . randint ( 0 , 3 )))
        tự . tốc độ  =  SPEED_GROUND
    
     cập nhật def ( tự , điểm ):
        tự . tốc độ  =  SPEED_GROUND  * ( 1  +  điểm / 500 )
        nếu  tự . tốc độ  >  SPEED_GROUND  *  2 :
            tự . tốc độ  =  SPEED_GROUND  *  2
        cho  tôi  trong  phạm vi ( len ( tự . danh sách )):
            tự . danh sách [ i ]. cập nhật ( tự . tốc độ )
        
        nếu  tự . danh sách [ 0 ]. x  <  - 132 :
            tự . danh sách . bật ( 0 )
            nếu  tự . tốc độ  >  SPEED_GROUND  *  1.5 :
                rand  =  ngẫu nhiên . randint ( 0 , 5 )
                nếu  rand  ==  5 :
                    tự . danh sách . append ( Bird ( tự . danh sách [ 1 ]. x  +  ngẫu nhiên . randint ( DISTANCE_MIN  +  200 , DISTANCE_MAX  +  100 ), ngẫu nhiên . lựa chọn (( Y_BIRD_1 , Y_BIRD_2 , Y_BIRD_3 ))))
                khác :
                    tự . danh sách . append ( Catus ( tự . danh sách [ 1 ]. x  +  ngẫu nhiên . randint ( DISTANCE_MIN  +  100 , DISTANCE_MAX  +  100 ), Y_CATUS , ngẫu nhiên . randint ( 0 , 4 )))
            khác :
                tự . danh sách . append ( Catus ( tự . danh sách [ 1 ]. x  +  ngẫu nhiên . randint ( DISTANCE_MIN , DISTANCE_MAX ), Y_CATUS , ngẫu nhiên . randint ( 0 , 3 )))
    
    def  vẽ ( tự ):
        cho  tôi  trong  phạm vi ( len ( tự . danh sách )):
            tự . danh sách [ i ]. vẽ ()



lớp  đất ():
    def  __init__ ( tự ):
        tự . x  =  0
        tự . y  =  138
        tự . img  =  IMG_GROUND
        tự . tốc độ  =  SPEED_GROUND
    
     cập nhật def ( tự , điểm ):
        tự . tốc độ  =  SPEED_GROUND  * ( 1  +  điểm / 500 )
        nếu  tự . tốc độ  >  SPEED_GROUND  *  2 :
            tự . tốc độ  =  SPEED_GROUND  *  2
        tự . x  - =  int ( tự . tốc độ )
        nếu  tự . x  <=  - 600 :
            tự . x  + =  600
    
    def  vẽ ( tự ):
        HIỂN THỊ . blit ( tự . img , ( tự . x , tự . y ))


lớp  Sky ():
    def  __init__ ( tự ):
        tự . x  =  0
        tự . y  =  0
        tự . tốc độ  =  TỐC ĐỘ
        tự . img  =  IMG_SKY
    
     cập nhật def ( tự , điểm ):
        tự . tốc độ  =  SPEED_SKY  * ( 1  +  điểm / 500 )
        nếu  tự . tốc độ  >  TỐC ĐỘ_KY  *  2 :
            tự . tốc độ  =  TỐC ĐỘ_KY  *  2
        tự . x  - =  int ( tự . tốc độ )
        nếu  tự . x  <=  - 600 :
            tự . x  + =  600
    
    def  vẽ ( tự ):
        HIỂN THỊ . blit ( tự . img , ( tự . x , tự . y ))


 Điểm số lớp ():
    def  __init__ ( tự ):
        tự . điểm  =  0
        tự . highScore  =  0
        tự . textScore  =  ""
        tự . textHighScore  =  ""
        tự . kích thước  =  15

     cập nhật def ( tự ):
        tự . điểm  + =  0,15
        nếu  tự . điểm  >  tự . highScore :
            tự . Xếp hạng  =  int ( tự . điểm )

        tự . textScore  =  str ( int ( tự . score ))
        cho  i  trong  phạm vi ( 5  -  len ( self . textScore )):
            tự . textScore  =  '0'  +  tự . textScore

        tự . textHighScore  =  str ( int ( tự . highScore ))
        cho  tôi  trong  phạm vi ( 5  -  len ( tự . textHighScore )):
            tự . textHighScore  =  '0'  +  tự . textHighScore
        tự . textHighScore  =  "HI:"  +  tự . textHighScore
    
    def  vẽ ( tự ):
        fontObj  =  pygame . phông chữ . SysFont ( 'Consolas' , tự . Kích thước )

        textSurfaceScore  =  fontObj . kết xuất ( tự . textScore , True , ( 0 , 0 , 0 ))
        HIỂN THỊ . blit ( textSurfaceScore , ( 550 , 10 ))

        textSurfaceHighScore  =  fontObj . làm cho ( tự . textHighScore , Đúng , ( 60 , 60 , 60 ))
        HIỂN THỊ . blit ( textSurfaceHighScore , ( 450 , 10 ))

lớp  BlinkText ():
    def  __init__ ( tự , văn bản ):
        tự . văn bản  =  văn bản
        tự . Thời gian thay đổi  =  0
        tự . kích thước  =  18
        fontObj  =  pygame . phông chữ . SysFont ( 'Consolas' , tự . Kích thước )
        textSurface  =  fontObj . làm cho ( tự . văn bản , False , ( 0 , 0 , 0 ))
        tự . bề mặt  =  pygame . Bề mặt ( textSurface . Get_size ())
        tự . bề mặt . điền (( 255 , 255 , 255 ))
        tự . bề mặt . blit ( textSurface , ( 0 , 0 ))
        tự . bề mặt . set_colorkey (( 255 , 255 , 255 ))
        tự . alpha  =  255
     cập nhật def ( tự ):
        tự . alpha  =  abs ( int ( 255  -  tự . Thời gian thay đổi ))
        nếu  tự . Thay đổi thời gian  >  255 * 2 :
            tự . Thời gian thay đổi  =  0
        tự . Thời gian thay đổi  + =  5

    def  vẽ ( tự ):
        tự . bề mặt . set_alpha ( tự . alpha )
        HIỂN THỊ . blit ( tự . bề mặt , ( int ( WINDOWWIDTH / 2  -  tự . bề mặt . get_width () / 2 ), 100 ))

def  isCollision ( tRex , ls ):
    tRexMask  =  pygame . mặt nạ . from_surface ( tRex . bề mặt )
    cho  catusOrBird  trong  ls . danh sách :
        catusOrBird_mask  =  pygame . mặt nạ . from_surface ( catusOrBird . bề mặt )
        kết quả  =  tRexMask . chồng lấp ( catusOrBird_mask , ( catusOrBird . x  -  tRex . x , catusOrBird . y  -  tRex . y ))
        nếu  kết quả :
            trả lại  đúng
    trả về  sai

def  chính ():

    bầu trời  =  bầu trời ()
    mặt đất  =  mặt đất ()
    tRex  =  T_Rex ( 0 )
    lên  =  sai
    xuống  =  Sai
    ls  =  ListCatusAndBirds ()
    điểm  =  Điểm ()
    blinkText  =  BlinkText ( "Nhấn UP để chơi" )
    trong khi  Đúng :
        isStart  =  Sai
        cho  sự kiện  trong  pygame . sự kiện . nhận ():
            nếu  sự kiện . loại  ==  QUIT  hoặc ( sự kiện . loại  ==  KEYUP  và  sự kiện . key  ==  K_ESCAPE ):
                trăn . bỏ ()
                sys . thoát ()
            nếu  sự kiện . loại  ==  KEYDOWN  và  sự kiện . khóa  ==  K_UP :
                lên  =  đúng
                isStart  =  Đúng
        nếu là  Bắt đầu :
            phá vỡ
        bầu trời . vẽ ()
        mặt đất . vẽ ()
        tRex . vẽ ()
        điểm số . vẽ ()
        nhấp nháy . cập nhật ()
        nhấp nháy . vẽ ()
        trăn . hiển thị . cập nhật ()
        FPSCLOCK . đánh dấu ( FPS )

    trong khi  Đúng :
        cho  sự kiện  trong  pygame . sự kiện . nhận ():
            nếu  sự kiện . loại  ==  QUIT  hoặc ( sự kiện . loại  ==  KEYUP  và  sự kiện . key  ==  K_ESCAPE ):
                trăn . bỏ ()
                sys . thoát ()
            nếu  sự kiện . loại  ==  TỪ KHÓA :
                nếu  sự kiện . khóa  ==  K_UP :
                    lên  =  đúng
                 sự kiện elif . khóa  ==  K_DOWN :
                    xuống  =  Đúng
            nếu  sự kiện . loại  ==  TỪ KHÓA :
                nếu  sự kiện . khóa  ==  K_UP :
                    lên  =  sai
                 sự kiện elif . khóa  ==  K_DOWN :
                    xuống  =  Sai
        
        bầu trời . cập nhật ( điểm . điểm )
        bầu trời . vẽ ()

        mặt đất . cập nhật ( điểm . điểm )
        mặt đất . vẽ ()

        tRex . cập nhật ( lên , xuống )
        tRex . vẽ ()

        ls . cập nhật ( điểm . điểm )
        ls . vẽ ()

        điểm số . cập nhật ()
        điểm số . vẽ ()

        if  isCollision ( tRex , ls ):
            tRex . bề mặt . điền (( 0 , 0 , 0 , 0 ))
            tRex . bề mặt . blit ( tRex . img , ( 0 , 0 ), ( 120 , 0 , 40 , 43 ))
            gameOverFontObj  =  pygame . phông chữ . SysFont ( 'consolas' , 30 , bold = 1 )
            gameOverTextSurface  =  gameOverFontObj . kết xuất ( "TRÒ CHƠI TRÊN" , Đúng , ( 0 , 0 , 0 ))
            trong khi  Đúng :
                isStart  =  Sai
                cho  sự kiện  trong  pygame . sự kiện . nhận ():
                    nếu  sự kiện . loại  ==  QUIT  hoặc ( sự kiện . loại  ==  KEYUP  và  sự kiện . key  ==  K_ESCAPE ):
                        trăn . bỏ ()
                        sys . thoát ()
                    nếu  sự kiện . loại  ==  KEYDOWN  và  sự kiện . khóa  ==  K_UP :
                        lên  =  đúng
                        isStart  =  Đúng
                nếu là  Bắt đầu :
                    phá vỡ
                bầu trời . vẽ ()
                mặt đất . vẽ ()
                tRex . vẽ ()
                ls . vẽ ()
                điểm số . vẽ ()
                HIỂN THỊ . blit ( gameOverTextSurface , ( int ( WINDOWWIDTH / 2  -  gameOverTextSurface . get_creen () / 2 ), 50 ))
                nhấp nháy . cập nhật ()
                nhấp nháy . vẽ ()
                trăn . hiển thị . cập nhật ()
                FPSCLOCK . đánh dấu ( FPS )
            điểm số . điểm  =  0
            ls  =  ListCatusAndBirds ()

        trăn . hiển thị . cập nhật ()
        FPSCLOCK . đánh dấu ( FPS )

if  __name__  ==  '__main__' :
    chính ()
