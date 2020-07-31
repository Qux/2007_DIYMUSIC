inlets = 2
outlets = 2


var queue = []
var numQueue = 0;

function clear() {
    queue.length = 0;
    numQueue = 0;
    outlet(1, "empty");
}

function bang() {
    switch (inlet) {
        case 0:
            if(0 != queue.length)   {
                outlet(1, queue.length);
                outlet(0, queue.shift());        
                numQueue--;        
            } else {
                outlet(1, "empty");
                numQueue = 0;
            }            
            break;
        case 1:
            break;
        default:
            break;
    }
}

function anything() {
    switch (inlet) {
        case 0:
            numQueue++;
            var a = arrayfromargs(messagename, arguments);            
            if(numQueue == 1)   {
                outlet(1, 0);
                outlet(0, a);    
            } else {
                queue.push(a);            
                outlet(1, queue.length);
            }                  
            break;        
        default:
            break;
    }
}


