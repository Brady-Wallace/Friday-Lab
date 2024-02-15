import maya.cmds as cmds

            
class Window(object):
    
    def __init__(self):
        self.window = "Window"
        self.title = "Renamer"
        self.size = (100,100)
        
        if cmds.window(self.window,exists=True):
            cmds.deleteUI(self.window,window=True)
            
        self.window = cmds.window(self.window,title=self.title, widthHeight = self.size)
        
        
        cmds.columnLayout(adjustableColumn =True)
        cmds.text("Select objects in order you want to be sequentially renamed. Type the name you want for the objects below.")
        cmds.separator(height=20)
        
        self.name = cmds.textField()
        
        self.initializeRename = cmds.button(label = 'Go', command = self.SequentialRenamer)
        
        cmds.showWindow()
    
  

    def SequentialRenamer(self,*args):
        
        string = cmds.textField(self.name, query = True, text = True)
        
               
        if "#" not in string:
            print( "please input a valid name: such as Leg_##_Jnt")

        else:
            maya_select_lyst = cmds.ls(selection=True)
            string.partition("##")
            for count,object in enumerate(maya_select_lyst):
                cmds.rename(object, string.partition("#")[0] + str(count + 1).zfill(string.count("#")) + string.rpartition("#")[2])
        
newWindow = Window()
     