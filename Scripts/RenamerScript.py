import maya.cmds as cmds

def SequentialRenamer(string):
    if "#" not in string:
        print( "please input a valid name")

    else:
        maya_select_lyst = cmds.ls(selection=True)
        string.partition("##")
        for count,object in enumerate(maya_select_lyst):
            cmds.rename(object, string.partition("#")[0] + str(count + 1).zfill(string.count("#")) + string.rpartition("#")[2])

SequentialRenamer("Leg_#_Jnt")
 