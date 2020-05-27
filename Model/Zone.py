class Zone:
    MAP_OFFSET_X=250
    MAP_OFFSET_Y=90

    GRID_WIDTH=80
    GRID_HEIGHT=90

    GRID_X_NUM=9
    GRID_Y_NUM=5

    @staticmethod
    def getIndex(x,y):
        X=(x-Zone.MAP_OFFSET_X)//Zone.GRID_WIDTH
        Y=(y-Zone.MAP_OFFSET_Y)//Zone.GRID_HEIGHT
        return X,Y

    @staticmethod
    def getGridPos(x,y):
        return x*Zone.GRID_WIDTH+Zone.MAP_OFFSET_X,y*Zone.GRID_HEIGHT+Zone.MAP_OFFSET_Y

    @staticmethod
    def isGrass(x,y):
        if x>=Zone.MAP_OFFSET_X and x<=Zone.MAP_OFFSET_X+Zone.GRID_WIDTH*9 and y>=Zone.MAP_OFFSET_Y and y<=Zone.MAP_OFFSET_Y+5*Zone.GRID_HEIGHT:
            return True
        else:
            return False







