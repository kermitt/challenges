const {log, verdict2} = require('./Tester')

function dirReduc() {
    return ["WEST"]
}


verdict2(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]), ["WEST"])
// verdict(dirReduc(["NORTH", "WEST", "SOUTH", "EAST"]), ["NORTH", "WEST", "SOUTH", "EAST"])
// verdict(dirReduc(["NORTH", "SOUTH", "EAST", "WEST", "EAST", "WEST"]), [])


