/*
 * Java implementation of a fly swatter simulator using Processing
 */

int randomSpeed = 10;

int fly_length = 100;  
int fly_xpos = 0;
int fly_ypos = 0;
float fly_xspeed = 1;
float fly_yspeed = 1;

boolean gameWon = false;

/***** Image variables *****/

PImage winImage;
PImage fly;
PImage swatterNeutral;
PImage swatterSmacked;
PImage kitchen;
    
void setup() {    
    
  size(960, 640);
  
  // Fly starts in the middle of the screen
  fly_xpos = width/2;
  fly_ypos = height/2;
  
  /*************** Load images (Creative Commons CC0) ***************/
  
  // https://pixabay.com/en/trophy-win-prize-transparent-1414791/
  winImage = loadImage("winner.png");
  winImage.resize(width, height);
  
  // https://pixabay.com/en/fly-cartoon-isolated-art-insect-309576/
  fly = loadImage("fly.png");
  fly.resize(fly_length, fly_length);
  
  // Image from https://pixabay.com/en/kitchen-real-estate-interior-design-1940177/
  kitchen = loadImage("kitchen.jpg");
  kitchen.resize(width, height);
  
  // Personal images
  swatterNeutral = loadImage("swatter.png");
  swatterNeutral.resize(fly_length, fly_length);
  swatterSmacked = loadImage("swatter_smack.png");
  swatterSmacked.resize(fly_length, fly_length);

}


void draw() {
  
  if (!gameWon) {
    
    background(kitchen);
    
    // Draw the fly and swatter
    image(fly, fly_xpos, fly_ypos);
    image(swatterNeutral, mouseX, mouseY);
    
    updateFlyPosition();
    
  }

}


void mousePressed() {
  
  if (!gameWon) {
    
      // Show swatter smacked image
      image(swatterSmacked, mouseX, mouseY);
      
      // Check if user clicked within boundary of fly image
      if (0 <= (mouseX-fly_xpos) && (mouseX-fly_xpos) <= fly_length && 0 <= (mouseY-fly_ypos) && (mouseY-fly_ypos)<= fly_length) {
          background(winImage);
          gameWon = true;
      }
          
  }          
}


void updateFlyPosition() {

  randomizeFlySpeed();
  
  // Update the position of the fly
  fly_xpos += fly_xspeed;
  fly_ypos += fly_yspeed;

  checkBoundary();
  
}


void randomizeFlySpeed() {
    
  // Add a random direction and speed
  float newfly_xspeed = fly_xspeed + random(-randomSpeed, randomSpeed);
  float newfly_yspeed = fly_yspeed + random(-randomSpeed, randomSpeed);
  
  // Prevent the fly from going too fast (At most 3 times randomSpeed)
  if (abs(newfly_xspeed) <= 3*randomSpeed) fly_xspeed = newfly_xspeed;
  if (abs(newfly_yspeed) <= 3*randomSpeed) fly_yspeed = newfly_yspeed;
  
}


void checkBoundary() {

  // If fly hits the window boundary, move it back towards the middle
  if (fly_xpos <= 0 || fly_xpos >= width-fly_length) {
    fly_xspeed *= -1;
    fly_xpos += fly_xspeed;
  }
  
  if (fly_ypos <= 0 || fly_ypos >= height-fly_length) {
    fly_yspeed *= -1;
    fly_ypos += fly_yspeed;
  }
    
}