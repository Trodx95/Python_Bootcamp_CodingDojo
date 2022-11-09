



class Phone:
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight

    def info(self):
        print(f"color: {self.color}")
        print(f"color: {self.weight}")
        return self
    
    def call(self, number):
        print("making a phone call")
        return self

    def ring(self):
        print("ringing ringing ringing ")
        return self

    def hang_up(self):
        print("hanging up")
        return self

    class CellPhone( Phone ):
        def __init__(self, color, weight):
            super().__init__(color, weight)
            self.type = "Cell Phone"

        def info(self):
            super().info()
            print(f"type: {self.type}")
            return self 

        def text(self , number ,msg):
            print(f"sending {number} the message: {msg}")
            return self

    class FlipCellPhone( CellPhone ):
        def __init__(self, color, weight):
            super().__init__(color, weight)
            self.flip_status ="close"
        
        def info(self):
            super().info()
            print(f"flipped status: {self.flip_status}")
            return self

        def flipped_closed(self):
            self.flip_status ="closed"
            return self

        def flipped_open(self):
            self.flip_status ="open"
            return self

        def call(self, number):
            if self.flip_status =='close':
                print("must open phone first")
            else:
                super().call(number)
                return self

    phone1= FlipCellPhone("blue", 5)

    phone1.info().flipped_open().call(1234567890).text(1234322322, "just sending this as a reminder")
        
