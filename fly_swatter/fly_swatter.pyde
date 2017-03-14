randomSpeed = 10;

fly_length = 100      
fly_xpos = 0
fly_ypos = 0
fly_xspeed = 1; 
fly_yspeed = 1;  
fly_xdirection = 1;  # 1 = Right, -1 = Left
fly_ydirection = 1;  # 1 = Down,  -1 = Up

gameWon = False;

###### Image variables ######
winImage = None
fly = None
swatterNeutral = None
swatterSmacked = None
kitchen = None
    
def setup():     
    
  global fly_xpos, fly_ypos, winImage, fly, maskImage, swatterNeutral, swatterSmacked, kitchen
  
  size(960, 640)
  frameRate(30)
  
  # Fly starts in the middle of the screen
  fly_xpos = width/2
  fly_ypos = height/2
  
  ################# Load images (Creative Commons CC0) #################
  
  # https://pixabay.com/en/trophy-win-prize-transparent-1414791/
  winImage = loadImage("winner.png")
  winImage.resize(width, height)
  
  # https://pixabay.com/en/fly-cartoon-isolated-art-insect-309576/
  fly = loadImage("fly.png")
  fly.resize(fly_length, fly_length)
  
  # Image from https://pixabay.com/en/kitchen-real-estate-interior-design-1940177/
  kitchen = loadImage("kitchen.jpg")
  kitchen.resize(width, height)
  
  # Personal images
  swatterNeutral = loadImage("swatter.png")
  swatterNeutral.resize(fly_length, fly_length)
  swatterSmacked = loadImage("swatter_smack.png")
  swatterSmacked.resize(fly_length, fly_length)

def draw():
  
  global fly_xpos, fly_ypos, gameWon, fly, swatterNeutral, kitchen
  
  if not gameWon:
    background(kitchen);
    
    # Draw the fly and swatter
    image(fly, fly_xpos, fly_ypos)
    image(swatterNeutral, mouseX, mouseY)
    
    updateFlyPosition()
    


def mousePressed():
  global fly_xpos, fly_ypos, fly_length, gameWon, swatterNeutral, swatterSmacked, winImage
  
  if not gameWon:    
      # Show swatter smacked image
      image(swatterSmacked, mouseX, mouseY)
      
      # Check if user clicked within boundary of fly image
      if (0 <= (mouseX-fly_xpos) <= fly_length and 0 <= (mouseY-fly_ypos) <= fly_length):
          fly_xpos = width*2
          fly_xspeed = 0
          image(swatterNeutral, fly_xpos, fly_ypos)
          background(winImage)
          gameWon = True
    
def updateFlyPosition():

  global fly_length, fly_xpos, fly_ypos, fly_xspeed, fly_yspeed, fly_xdirection, fly_ydirection

  randomizeFlySpeed()
  
  # Update the position of the fly
  fly_xpos += fly_xspeed * fly_xdirection
  fly_ypos += fly_yspeed * fly_ydirection

  # If fly hits the window boundary, move it back towards the middle
  if (fly_xpos <= 0 or fly_xpos >= width-fly_length):
    fly_xdirection *= -1;
    fly_xpos += fly_xspeed * fly_xdirection
  
  if (fly_ypos <= 0 or fly_ypos >= height-fly_length):
    fly_ydirection *= -1;
    fly_ypos += fly_yspeed * fly_ydirection

def randomizeFlySpeed():
    
  global fly_xspeed, fly_yspeed, randomSpeed

  # Add a random direction and speed
  newfly_xspeed = fly_xspeed + random(-randomSpeed, randomSpeed)
  newfly_yspeed = fly_yspeed + random(-randomSpeed, randomSpeed)
  
  # Prevent the fly from going too fast (At most 3 times randomSpeed)
  if (abs(newfly_xspeed) <= 3*randomSpeed): fly_xspeed = newfly_xspeed
  if (abs(newfly_yspeed) <= 3*randomSpeed): fly_yspeed = newfly_yspeed
