import maya.cmds as cmds

constraints = cmds.ls(type='parentConstraint')
cmds.select (constraints, r=True)

for i in constraints:
    cmds.setAttr(i+".interpType",2)
 