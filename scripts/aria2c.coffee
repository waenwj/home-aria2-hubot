child_process = require('child_process')



module.exports = (robot) ->
  robot.respond /baseinfo/i, (res) ->

    data = JSON.stringify({
      user_id: res.message.user.id,
      user_name: res.message.user.name,
      message: res.message,
    })
    res.send data

  robot.respond /aria2c (\w+)([ ]*)(.*)/i, (res) ->
    command = res.match[1]
    arg = res.match[3]
    child_process.exec "python action/aria2c.py \"#{command}\" \"#{arg}\"",  (error, stdout, stderr) ->
      res.send stdout
      res.send stderr

  robot.respond /info/i, (res) ->
    child_process.exec "python action/info.py",  (error, stdout, stderr) ->
      res.send stdout
      res.send stderr
 
  robot.respond /add (.*)/i, (res) ->
    uri = res.match[1]
    if uri 
      child_process.exec "python action/add.py \"#{uri}\"",  (error, stdout, stderr) ->
        res.send stdout
        res.send stderr
    else 
      res.reply 'Lack URI'
