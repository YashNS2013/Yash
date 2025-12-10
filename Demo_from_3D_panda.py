from direct.showbase.ShowBase import ShowBase


class my_game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.disableMouse()
        self.camera.setPos(0, -10, 2)
        self.camera.lookAt(0, 0, 1)


        self.panda = self.loader.loadModel("models/panda-model")
        self.panda.reparentTo(self.render)
        self.panda.setScale(0.005)
        self.panda.setPos(0, 0, 0)
        self.setBackgroundColor(0.6, 0.8, 1.0)

        
        self.taskMgr.add(self.spin_panda, "SpinPandaTask")

    def spin_panda(self, task):
        self.panda.setH(self.panda.getH() + 50 * globalClock.getDt())
        return task.cont

game = my_game()
game.run()