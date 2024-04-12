import board
from PIL import Image, ImageDraw, ImageFont, ImageOps
import adafruit_ssd1306
import time

class Display:
    
    WIDTH = 128
    HEIGHT = 64
    
    def __init__(self):
        self.__i2c = board.I2C()
        self.__oled = adafruit_ssd1306.SSD1306_I2C(self.WIDTH, self.HEIGHT, self.__i2c)
        
        self.__header_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)
        self.__body_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)
        
        self.setup_images()
        
        self.__image = Image.new("1", (self.WIDTH, self.HEIGHT))
        self.__draw = ImageDraw.Draw(self.__image)
        
        self.__header_strip()
        self.wait()
        
    def clear(self):
        self.__oled.fill(0)
        self.__oled.show()
        
    def update_time(self):
        time_str = time.strftime("%H:%M")
        (time_width, time_height) = self.__header_font.getsize(time_str)
        self.__draw.text((128 - time_width, 0), time.strftime("%H:%M"), font=self.__header_font, fill=1)
        
    def wait(self):
        self.__clear_body()
        self.__draw.text((5, 29), "Standby...", font=self.__body_font, fill=1)
        self.__show_image()
        
    def success(self):
        self.__clear_body()
        self.__draw.text((5, 21), "Access", font=self.__body_font, fill=1)
        self.__draw.text((5, 39), "granted!", font=self.__body_font, fill=1)
        self.__image.paste(self.__success_image, (85, 23))
        self.__show_image()
        
    def welcome(self, name: str):
        self.__clear_body()
        self.__draw.text((5, 21), "Welcome,", font=self.__body_font, fill=1)
        self.__draw.text((5, 39), name, font=self.__body_font, fill=1)
        self.__image.paste(self.__welcome_image, (85, 23))
        self.__show_image()
        
    def fail(self):
        self.__clear_body()
        self.__draw.text((5, 21), "Access", font=self.__body_font, fill=1)
        self.__draw.text((5, 39), "denied!", font=self.__body_font, fill=1)
        self.__image.paste(self.__fail_image, (85, 23))
        self.__show_image()
        
    def setup_images(self):
        yes_image = Image.open("images/yes.jpeg").resize((self.HEIGHT // 2, self.HEIGHT // 2), Image.BICUBIC).convert("L")
        self.__success_image = ImageOps.invert(yes_image).convert("1")
        welcome_image = Image.open("images/pi.png").resize((self.HEIGHT // 2, self.HEIGHT // 2), Image.BICUBIC).convert("L")
        self.__welcome_image = ImageOps.invert(welcome_image).convert("1")
        self.__fail_image = Image.open("images/no.jpeg").resize((self.HEIGHT // 2, self.HEIGHT // 2), Image.BICUBIC).convert("1")
    
    def __header_strip(self):
        self.__draw.rectangle((0, 15, 128, 15), fill=1)
        
    def __clear_body(self):
        self.__draw.rectangle((0, 16, 127, 63), fill=0)
        
    def __show_image(self):
        self.update_time()
        self.__oled.image(self.__image)
        self.__oled.show()
        

if __name__ == "__main__":
    display = Display()
    time.sleep(5)
    display.success()
    time.sleep(5)
    display.welcome("Ilya")
    time.sleep(5)
    display.fail()
    time.sleep(5)
    display.clear()
