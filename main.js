var ads1x15 = require('node-ads1x15'), i2c=require('i2c-bus'), MPU6050 = require('i2c-mpu6050');

var mpu6050_address = 0x68;
var i2c1 = i2c.openSync(1);
var motionsensor = new MPU6050(i2c1, mpu6050_address);


var adc = new ads1x15(1);
var channel = 0; //channel 0, 1, 2, or 3...
var samplesPerSecond = '250'; // see index.js for allowed values for your chip
var progGainAmp = '4096'; // see index.js for allowed values for your chip


var lightdata = 0;
var motiondata = 0;
var tempdata = 0;

var x,y,z; //accel readings
var px=0,py=0,pz=0; //previous accel readings
var mx, my, mz; //momentum
var motion; //combined momentum

var startingtime = new Date().getTime();
var currenttime;
var intervaltime = 0;

function getData(){

  adc.readADCSingleEnded(0, progGainAmp, samplesPerSecond, function(err, data0) {
  currenttime=new Date().getTime()-startingtime; // get offset
    if(intervaltime==0||(currenttime-intervaltime>122)){

    lightdata=Math.round(((Math.abs(data0-4094))/4094)*127)
    motiondata=motionsensor.readSync();
    tempdata=Math.round(Math.abs(motiondata.temp/40)*127);

    x=motiondata.accel.x;
    y=motiondata.accel.y;
    z=motiondata.accel.z;
    mx=Math.abs(px-x);
    my=Math.abs(py-y);
    mz=Math.abs(pz-z);


    motion=Math.round((Math.abs(mx+my+mz)/8)*127)
      console.log(currenttime-intervaltime+";"+motion+";"+tempdata+";"+lightdata);
      if(currenttime-intervaltime>250){
        console.log("WARNING - Spike Detected, Interval Time: "+currenttime-intervaltime);
      }
      intervaltime=currenttime;
      px=x;
      py=y;
      pz=z;
    }
    getData();
    });

}
getData();
