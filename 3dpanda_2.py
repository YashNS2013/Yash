from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import AmbientLight, DirectionalLight
import random

class CartoonAnimation(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.disableMouse()
        self.setBackgroundColor(0.6, 0.8, 1.0)
        self.camera.setPos(0, -40, 10)
        self.camera.lookAt(0, 0, 5)

        # Lighting
        ambientLight = AmbientLight("ambientLight")
        ambientLight.setColor((0.7, 0.7, 0.7, 1))
        directionalLight = DirectionalLight("directionalLight")
        directionalLight.setDirection((-5, -5, -5))
        directionalLight.setColor((0.8, 0.8, 0.8, 1))
        self.render.setLight(self.render.attachNewNode(ambientLight))
        self.render.setLight(self.render.attachNewNode(directionalLight))

        # Load panda model and animation
        self.panda = self.loader.loadModel("models/panda")
        self.panda.reparentTo(self.render)
        self.panda.setScale(0.2)
        self.panda.setPos(-10, 0, 0)

        # Panda walk animation (simulate by moving position)
        self.direction = 1

        # Add a task to animate the panda and background
        self.elapsed = 0
        self.taskMgr.add(self.animate_scene, "AnimateSceneTask")

    def animate_scene(self, task):
        dt = globalClock.getDt()
        self.elapsed += dt

        # Move panda left and right
        x = self.panda.getX() + self.direction * dt * 2
        if x > 10:
            self.direction = -1
        elif x < -10:
            self.direction = 1
        self.panda.setX(x)

        # Change background color every 30 seconds
        if int(self.elapsed) % 30 == 0:
            self.setBackgroundColor(random.random(), random.random(), 1.0)

        # Move camera slowly for effect
        cam_x = 20 * (self.elapsed % 60) / 60 - 10
        self.camera.setPos(cam_x, -40, 10)
        self.camera.lookAt(0, 0, 5)

        # End after 5 minutes (300 seconds)
        if self.elapsed > 300:
            self.userExit()
            return Task.done

        return Task.cont

app = CartoonAnimation()
app.run()