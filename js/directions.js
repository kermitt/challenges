const {log, verdict} = require('./Tester')

function dirReduc() {
    return ["WEST"]
}


verdict(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]), ["WEST"])
verdict(dirReduc(["NORTH", "WEST", "SOUTH", "EAST"]), ["NORTH", "WEST", "SOUTH", "EAST"])
verdict(dirReduc(["NORTH", "SOUTH", "EAST", "WEST", "EAST", "WEST"]), [])


