import play

play.set_backdrop("darkorange")

#circle
ball = play.new_circle(x = -300 ,y = -250, radius = 20 , color = "green")
#walls
wall1 = play.new_box(x = -300, y = 0, width = 200, height = 10, color = "black")
wall2 = play.new_box(x = -100, y = 0, width = 200, height = 10, color = "black")
wall3 = play.new_box(x = -200, y = 100, width = 10, height = 200, color = "black")
wall4 = play.new_box(x = 200, y = -100, width = 10, height = 200, color = "black")
wall5 = play.new_box(x = 300, y = -200, width = 200, height = 10, color = "black")
wall6 = play.new_box(x = 100, y = -200, width = 200, height = 10, color = "black")
wall7 = play.new_box(x = 300, y = 200, width = 200, height = 10, color = "black")
wall8 = play.new_box(x = 100, y = 200, width = 200, height = 10, color = "black")
wall9 = play.new_box(x = -400, y = -200, width = 150, height = 10, color = "black")
wall10 = play.new_box(x = -250, y = -200, width = 150, height = 10, color = "black")
wall11 = play.new_box(x = 0, y = 20, width = 10, height = 50, color = "black")
wall12 = play.new_box(x = 0, y = 40, width = 10, height = 50, color = "black")
#text
finish = play.new_text(words = "FINISH", x = -300, y = 50, font = None, font_size = 70 , color = "green" )
#-------------------------------

@play.when_program_starts
def start():
  ball.start_physics(bounciness=1.5)
  wall1.start_physics(can_move = False)
  wall2.start_physics(can_move = False)
  wall3.start_physics(can_move = False)
  wall4.start_physics(can_move = False)
  wall5.start_physics(can_move = False)
  wall6.start_physics(can_move = False)
  wall7.start_physics(can_move = False)
  wall8.start_physics(can_move = False)
  wall9.start_physics(can_move = False)
  wall10.start_physics(can_move = False)
  wall11.start_physics(can_move = False)
  wall12.start_physics(can_move = False)

@play.repeat_forever
def do():
  ball.physics.y_speed = 0
  ball.physics.x_speed = 0

  if play.key_is_pressed('w'):
    ball.physics.y_speed = 10
  if play.key_is_pressed('s'):
    ball.physics.y_speed = -10
  if play.key_is_pressed('a'):
    ball.physics.x_speed = -10
  if play.key_is_pressed('d'):
    ball.physics.x_speed = 10
  if ball.is_touching(finish):
    wall1.hide()
    wall2.hide()
    wall3.hide()
    wall4.hide()
    wall5.hide()
    wall6.hide()
    wall7.hide()
    wall8.hide()
    wall9.hide()
    wall10.hide()
    wall11.hide()
    wall12.hide()
    finish.hide()
    ball.hide()
    play.new_text(words="YOU WIN", x = 0 , y =0, font = None, font_size= 100, color = "red") 
  


play.start_program()
