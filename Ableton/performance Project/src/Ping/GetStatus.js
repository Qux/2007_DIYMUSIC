inlets = 1;
outlets = 1;

var Low_Threath = 300;
var High_Threath = 800;

var Status = {
    Fast:0,
    Normal:1,
    Slow:2,
};

function msg_float(val) {
    if(val < Low_Threath)   {
        outlet(0, Status.Fast);
    } else if (High_Threath < val) {
        outlet(0, Status.Slow);
    } else {
        outlet(0, Status.Normal);
    }
}