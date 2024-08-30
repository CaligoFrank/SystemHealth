
import customtkinter
import subprocess
import psutil
import win32com.client



#First need to make a dynamic Function that gets and returns the Disk usage




class Frame(customtkinter.CTkFrame):
    """Frame Object meant for organizing widgets within frames.
    
    Args:
        master (CTk Object): The parent widget.
        title (str, optional): Title text for the frame. If not provided, no title label will be created.
    """
    def __init__(self, master, title=None):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        
        if title:
            self.title = title
            self.title_label = customtkinter.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
            self.title_label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")
        else:
            self.title_label = None



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        #TODO Add functions up here

        self.title("System Health")
        self.geometry("480x480")
#FRAMES-----FRAMESFRAMES-----FRAMESFRAMES-----FRAMESFRAMES-----FRAMESFRAMES-----FRAMESFRAMES-----FRAMESFRAMES-----FRAMESFRAMES-----FRAMESFRAMES-----FRAMES
        #Making of the frame for Disk info
        self.DiskInfoFrame= Frame(self, "Disk Info")
        self.DiskInfoFrame.grid(row = 0, column = 0)

        #Make the inner frame to have everyhting centered within the Disk Info Frame
        self.DiskInfoInnerFrame = Frame(self.DiskInfoFrame)
        self.DiskInfoInnerFrame.grid(row = 1, column = 0)

        #CPU Frame Displaying the CPU percentage and information
        self.CPUFrame = Frame(self, "CPU Info")
        self.CPUFrame.grid(row = 0, column = 1, padx = 10, pady = 10)
        #Make the inner Frame for CPU
        self.CPUFrameInner = Frame(self.CPUFrame)
        self.CPUFrameInner.grid(row = 1 , column = 0)



        #Now for General System Health Frame
        self.SystemHealth = Frame(self, "General System Health")
        self.SystemHealth.grid(row = 0 , column = 2)
        #Inner System Health Frame
        self.SystemHealthInner = Frame(self.SystemHealth)
        self.SystemHealthInner.grid(row = 1, column = 0 )

        #Make the Boot Time Frame
        self.BootTimeFrame = Frame(self, "Boot Time")
        self.BootTimeFrame.grid(row = 2, column = 0)
        #Make the Inner Frame to keep everyhting centered
        self.BootTimeFrameInner = Frame(self.BootTimeFrame)
        self.BootTimeFrameInner.grid(row = 1, column = 0)
        
        #Creating the MEMORY Frame
        self.MemoryFrame = Frame(self, "Memory Info")
        self.MemoryFrame.grid(row = 2, column = 1)

        #Create the Memory Frame Inner
        self.MemoryFrameInner = Frame(self.MemoryFrame)
        self.MemoryFrameInner.grid(row = 1, column = 0)
        
        #Now Network Frame
        self.NetworkFrame = Frame(self, "Network Info")
        self.NetworkFrame.grid(row = 1, column = 2)
        #Making the Network Inner Frame
        self.NetworkFrameInner = Frame(self.NetworkFrame)
        self.NetworkFrameInner.grid(row = 1, column = 0 )
#FRAMES-----FRAMESFRAMES-----FRAMESFRAMES-----FRAMESFRAMES-----FRAMESFRAMES-----FRAMESFRAMES-----FRAMESFRAMES-----FRAMESFRAMES-----FRAMES

        #Now making of the disk space labels to be later configured
        self.TotalDiskSpaceLb = customtkinter.CTkLabel(self.DiskInfoInnerFrame, text="Total Disk Space: ")
        self.TotalDiskSpaceLb2 = customtkinter.CTkLabel(self.DiskInfoInnerFrame, text=None, bg_color="grey")

        self.UsedDiskSpaceLb = customtkinter.CTkLabel(self.DiskInfoInnerFrame, text="Used Disk Space: " )
        self.UsedDiskSpaceLb2 = customtkinter.CTkLabel(self.DiskInfoInnerFrame, text=None, bg_color="grey")

        self.FreeDiskSpaceLb = customtkinter.CTkLabel(self.DiskInfoInnerFrame, text="Free Disk Space: ")
        self.FreeDiskSpaceLb2 = customtkinter.CTkLabel(self.DiskInfoInnerFrame, text = None, bg_color="grey")

        self.DiskPercentageLb = customtkinter.CTkLabel(self.DiskInfoInnerFrame, text="Disk Percentage: ")
        self.DiskPercentageLb2 = customtkinter.CTkLabel(self.DiskInfoInnerFrame,text=None, bg_color="grey")

        #Now Place the Labels Since this is the first one on the Frame we Start with row 0  and col 0
        self.TotalDiskSpaceLb.grid(row = 0, column = 0)
        self.TotalDiskSpaceLb2.grid(row = 0, column = 1)

        self.UsedDiskSpaceLb.grid(row = 1, column = 0)
        self.UsedDiskSpaceLb2.grid(row = 1, column = 1)

        self.FreeDiskSpaceLb.grid(row = 2, column =  0)
        self.FreeDiskSpaceLb2.grid(row = 2, column = 1)

        self.DiskPercentageLb.grid(row = 3, column = 0)
        self.DiskPercentageLb2.grid(row = 3, column = 1)
#-----------------------------------------------------------------------------------------



        #These are the labels for the CPU Name, Clock Speed, and CPU Percentage

        self.CPUNameLb = customtkinter.CTkLabel(self.CPUFrameInner, text="CPU Name: ")
        self.CPUNameLb2 = customtkinter.CTkLabel(self.CPUFrameInner, text=None, bg_color="grey")

        self.CPUClockSpeedLb = customtkinter.CTkLabel(self.CPUFrameInner, text="Clock Speed: ")
        self.CPUClockSpeedLb2 = customtkinter.CTkLabel(self.CPUFrameInner, text=None, bg_color="grey")

        self.CPUPercentageLb = customtkinter.CTkLabel(self.CPUFrameInner, text = " CPU Percentage: ")
        self.CPUPercentageLb2 = customtkinter.CTkLabel(self.CPUFrameInner, text=None, bg_color="grey")

        #Place the Labels
        self.CPUNameLb.grid(row = 0, column = 0)
        self.CPUNameLb2.grid(row = 0, column = 1)

        self.CPUClockSpeedLb.grid(row = 1, column = 0)
        self.CPUClockSpeedLb2.grid(row = 1, column = 1)

        self.CPUPercentageLb.grid(row = 2, column = 0)
        self.CPUPercentageLb2.grid(row = 2, column = 1)




        #Labels for Free Disk Space, And that the CPU isnt overloaded
        #Has the Latest Secerity update
        #And that its running the appropriote services running

        self.SystHealthFreeDiskLb = customtkinter.CTkLabel(self.SystemHealthInner, text= "Free Disk Space:")
        self.SystHealthFreeDiskLb2 = customtkinter.CTkLabel(self.SystemHealthInner, text=None, bg_color="grey")

        self.SystemHealthCPUOverloadedlb = customtkinter.CTkLabel(self.SystemHealthInner, text="CPU Overloaded?: ")
        self.SystemHealthCPUOverloadedlb2 = customtkinter.CTkLabel(self.SystemHealthInner, text=None, bg_color="grey")

        self.SystemHealthSecurityUpdatesLb = customtkinter.CTkLabel(self.SystemHealthInner, text = "Up to Date?: ")
        self.SystemHealthSecurityUpdatesLb2 = customtkinter.CTkLabel(self.SystemHealthInner, text=None, bg_color="grey")

        #Now Placing the Labels from Above

        self.SystHealthFreeDiskLb.grid(row = 1, column = 0)
        self.SystHealthFreeDiskLb2.grid(row = 1, column = 1)

        self.SystemHealthCPUOverloadedlb.grid(row = 2, column = 0)
        self.SystemHealthCPUOverloadedlb2.grid(row = 2, column = 1)

        self.SystemHealthSecurityUpdatesLb.grid(row = 3, column = 0)
        self.SystemHealthSecurityUpdatesLb2.grid(row = 3, column = 1)
#------------------------------------------------------------------------------------------------------------------------------
        
        #Creating the Boot time labels 
        self.BootTimeLb = customtkinter.CTkLabel(self.BootTimeFrameInner, text="Boot Time: ")
        self.BootTimeLb2 = customtkinter.CTkLabel(self.BootTimeFrameInner, text=None, bg_color="grey")

        #Placing the Boot time labels
        self.BootTimeLb.grid(row = 1, column = 0)
        self.BootTimeLb2.grid(row = 1, column = 1)

        #Create the Memeory Labels
        self.TotalMemoryLb = customtkinter.CTkLabel(self.MemoryFrameInner, text="Total Memory: ")
        self.TotalMemoryLb2 = customtkinter.CTkLabel(self.MemoryFrameInner, text = None, bg_color="grey")

        self.AvailableMemoryLb = customtkinter.CTkLabel(self.MemoryFrameInner, text="Available Memory: ")
        self.AvailableMemoryLb2 = customtkinter.CTkLabel(self.MemoryFrameInner, text = None, bg_color="grey")

        self.UsedMemoryLb = customtkinter.CTkLabel(self.MemoryFrameInner, text="Used Memory: ")
        self.UsedMemoryLb2 = customtkinter.CTkLabel(self.MemoryFrameInner, text = None, bg_color="grey")

        self.PercentageMemoryLb = customtkinter.CTkLabel(self.MemoryFrameInner, text="Memory Percentage: ")
        self.PercentageMemoryLb2 = customtkinter.CTkLabel(self.MemoryFrameInner, text = None, bg_color="grey")
    
        #Placing memory Labels
        self.TotalMemoryLb.grid(row = 1, column = 0)
        self.TotalMemoryLb2.grid(row = 1, column = 1)

        self.AvailableMemoryLb.grid(row = 2, column = 0)
        self.AvailableMemoryLb2.grid(row = 2, column = 1)

        self.UsedMemoryLb.grid(row = 3, column = 0)
        self.UsedMemoryLb2.grid(row = 3, column = 1)

        self.PercentageMemoryLb.grid(row = 4, column = 0)
        self.PercentageMemoryLb2.grid(row = 4, column = 1)

        #Making Network Frame Labels
        self.NetWorkInterfaceLb = customtkinter.CTkLabel(self.NetworkFrameInner, text="Interface: ")
        self.NetWorkInterfaceLb2 = customtkinter.CTkLabel(self.NetworkFrameInner, text=None, bg_color="grey")

        self.NetWorkStatusLb = customtkinter.CTkLabel(self.NetworkFrameInner, text="Status: ")
        self.NetWorkStatusLb2 = customtkinter.CTkLabel(self.NetworkFrameInner, text=None, bg_color="grey")
        
        self.NetWorkSpeedLb = customtkinter.CTkLabel(self.NetworkFrameInner, text="Speed: ")
        self.NetWorkSpeedLb2 = customtkinter.CTkLabel(self.NetworkFrameInner, text=None, bg_color="grey")

        self.NetWorkMTULb = customtkinter.CTkLabel(self.NetworkFrameInner, text="MTU: ")
        self.NetWorkMTULb2 = customtkinter.CTkLabel(self.NetworkFrameInner, text=None, bg_color="grey")

        self.NetWorkAddressLb = customtkinter.CTkLabel(self.NetworkFrameInner, text="Address: ")
        self.NetWorkAddressLb2 = customtkinter.CTkLabel(self.NetworkFrameInner, text=None, bg_color="grey")

        self.NetWorkNetMaskLb = customtkinter.CTkLabel(self.NetworkFrameInner, text="NetMask: ")
        self.NetWorkNetMaskLb2 = customtkinter.CTkLabel(self.NetworkFrameInner, text=None, bg_color="grey")

        #Now Place the Labels

        self.NetWorkInterfaceLb.grid(row = 1, column = 0)
        self.NetWorkInterfaceLb2.grid(row = 1, column = 1)

        self.NetWorkStatusLbv
        self.NetWorkStatusLb2
        
        self.NetWorkSpeedLb
        self.NetWorkSpeedLb2

        self.NetWorkMTULb
        self.NetWorkMTULb2

        self.NetWorkAddressLb
        self.NetWorkAddressLb2

        self.NetWorkNetMaskLb
        self.NetWorkNetMaskLb2


        #Now for IO Stats
        self.IONetworkFrame = Frame(self.NetworkFrameInner, "IO Stats")
        self.IONetworkFrame.grid(row = 1, column = 3)









app = App()
app.mainloop()