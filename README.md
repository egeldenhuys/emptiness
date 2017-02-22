# Emptiness

Find empty venues on the University of Pretoria campus.

## Usage
### CLI
```
usage: emptiness.py [-h] [-d DAY] [-t TIME] [--version]

optional arguments:
  -h, --help            show this help message and exit
  -d DAY, --day DAY     Day to check the timetable on. (eg: Thursday)
  -t TIME, --time TIME  The time the venue must be empty. (eg: 15:30)
  --version             show program's version number and exit
```

#### Example output
```
$ python emptiness.py -d Thursday -t 13:30

GW/HB 1-14
GW/HB 1-9
GW/HB 14-02
GW/HB 3-14
Geografie/Geography 1-2
Groen/Green lab
Grys/Grey lab
Ing/Eng  A-Lab
Ing/Eng III - 6
Wisk/Maths 2-1
```

### Server
- `./start-allr.sh` - Start all daemons
- `./stop-all.sh` - Stop all daemons
- `./restart-all.sh` - Restart all daemons

## Requirements
- Python 3 (`pacman -S python`)
- pip (`pacman -S python-pip`)
	- [requests](http://docs.python-requests.org/en/master/user/install/) (`pip install requests`)
	- [Flask](http://flask.pocoo.org/) (`pip install Flask`)
