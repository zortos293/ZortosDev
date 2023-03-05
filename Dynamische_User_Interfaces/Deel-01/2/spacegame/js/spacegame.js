var consoleLog = console.log;

var SpaceShip = function () {

    // So we can reference this when we are inside other functions
    var self = this;
    // This wont be visible to the consumers of the spacegame instance
    var local = {};

    local.description = 'Behaal de finish';

    local.settings = {
        rows: 6,
        columns: 6,
        spaceSize: 80,
        speed: 300,
        start: [0,0],
        finish: false,
        showCoordinates: false,
        showGoals: true,
        orientation: 'bottom',
        belts : [],
        walls: [],
        spinners: [],
        pits: [],
        voids: [],
        colored: []
    };

    local.goals = {
    };

    local.orientations = ['bottom', 'right', 'top', 'left'];

    local.state = {
        ship: {
            orientation: local.orientations[0],
            deg: 0,
            position: local.settings.start,
        },
        goals : {},
        spun:0,
        finished: false,
        running: false,
        orignalProgrammerActionCount: 0,
        programmerActionCount: 0,
        actions: [],
        nextAction: null,
        lines: 0
    };

    local.stateList = [];

    local.objects = {
        container: container,
        board: null,
        ship: null,
        spaces: [],
        spinners: []
    };

    // ----------- [funtions to build the board] --------- //

    local.board = {};
    local.board.build = {};
    local.board.build.fieldGrid = function () {
        var div = document.createElement("div");
        div.id = 'board';

        local.objects.board = div;
        local.objects.container.appendChild(div);

        // set the grid
        local.objects.board.style.gridTemplateColumns = (local.settings.spaceSize+"px ").repeat(local.settings.columns);
        local.objects.board.style.gridTemplateRows = (local.settings.spaceSize+"px ").repeat(local.settings.rows);

        for (var i = 0; i < (local.settings.rows*local.settings.columns); i++) {
            var coordinates = local.space.getCoordinatesByIndex(i);
            local.space.build(coordinates[0],coordinates[1]);
            local.objects.board.appendChild(local.objects.spaces[coordinates[0]][coordinates[1]]);
        }
    };
    local.board.build.fieldObjects = function(){
        if(local.settings.finish != false){
            local.space.addClass(local.settings.finish[0], local.settings.finish[1], 'finish');
        }

        for (var i=0; i <local.settings.pits.length; i++){
            local.space.addClass(local.settings.pits[i][0], local.settings.pits[i][1], 'pit');
        }

        for (var i=0; i <local.settings.voids.length; i++){
            local.space.addClass(local.settings.voids[i][0], local.settings.voids[i][1], 'void');
        }

        for (var i=0; i <local.settings.colored.length; i++){
            local.space.addClass(local.settings.colored[i][0], local.settings.colored[i][1], 'colored');
        }

        for (var i=0; i <local.settings.walls.length; i++){
            for (var j=0; j <local.settings.walls[i][2].length; j++){
                local.space.addClass(local.settings.walls[i][0], local.settings.walls[i][1], 'wall-'+local.settings.walls[i][2][j]);
            }
        }

        for (var i=0; i <local.settings.belts.length; i++){
            var x = local.settings.belts[i][0];
            var y = local.settings.belts[i][1];

            local.space.addClass(x, y, 'belt');
            local.space.setData(x, y, 'direction', local.settings.belts[i][2]);
        }

        for (var i=0; i <local.settings.spinners.length; i++){
            var x = local.settings.spinners[i][0];
            var y = local.settings.spinners[i][1];

            var spinner = document.createElement('div');
            spinner.classList.add('spinner');
            spinner.classList.add(local.settings.spinners[i][2]);
            spinner.style.transitionDuration = (local.settings.speed-50)+'ms';

            local.space.getElement(x, y).appendChild(spinner);


            if(local.objects.spinners[x] == undefined){
                local.objects.spinners[x] = [];
            }

            local.objects.spinners[x][y] = spinner;
        }
    };
    local.board.build.goalsDisplay = function(){
        if(local.settings.showGoals) {
            var div = document.createElement("div");
            div.id = 'goals';
            div.classList.add('w-100');

            if(local.description.length > 0) {
                var h2 = document.createElement('h2');
                h2.innerHTML = local.description;
                div.appendChild(h2);
            }

            var goals = Object.entries(local.goals);

            for (var i=0; i<goals.length; i++) {
                var goal = document.createElement("div");
                goal.id = goals[i][0];
                goal.classList.add('goal');

                goal.innerHTML = goals[i][0]+': '+goals[i][1];

                div.appendChild(goal);
            }

            document.body.appendChild(div);
            local.objects.container.style.marginTop = (div.offsetHeight+5)+ 'px';
        }

    };
    local.board.build.actionBar = function(){
        var actionBar = document.createElement('div');
        actionBar.id = 'actionBar';
        actionBar.style.height = (local.settings.rows * local.settings.spaceSize)+ 'px';
        local.objects.container.appendChild(actionBar);
    };
    local.board.writeToActionBar = function(actionName, success){
        var action = document.createElement('div');
        action.style.transitionDuration = (local.settings.speed-50)+'ms';
        action.classList.add('action');

        var actionHover = document.createElement('div');

        if(success == false){
            action.classList.add('fail');
        }

        actionHover.innerHTML = actionName;
        action.appendChild(actionHover);

        document.getElementById('actionBar').appendChild(action);
        setTimeout(function(){
            action.style.height = ((local.settings.rows * local.settings.spaceSize)/local.state.orignalProgrammerActionCount)-2 + 'px';
        },30);
    };
    local.board.hasActions = function(){
        return local.settings.spinners.length > 0;
    };
    local.board.executeActions = function(){
        local.state.spun++;
        for (var i=0; i <local.settings.spinners.length; i++){
            var x = local.settings.spinners[i][0];
            var y = local.settings.spinners[i][1];
            var direction = local.settings.spinners[i][2];
            var deg = (90*local.state.spun) * (direction == "left"? -1 : 1);

            var elem = local.objects.spinners[x][y];
            elem.style.transform = 'rotate('+deg+'deg)';
            elem.style.webkitTransform = 'rotate('+deg+'deg)';

            if(local.space.containsShip(x,y)){
                local.ship.rotate[direction]();
            }
        }
    };
    local.board.createBanner = function(msg, type, subMessage) {
        var banner = document.createElement('div');
        banner.id = 'banner';
        banner.classList.add(type);

        var h2 = document.createElement('h2');
        h2.innerHTML = msg;
        banner.appendChild(h2);
        var span = document.createElement('span');
        span.classList.add('sub');

        if(subMessage != undefined){
            span.innerHTML = subMessage;
        }

        banner.appendChild(span);

        var removeBtn = document.createElement('img');
        removeBtn.src = 'images/cancel.png';
        removeBtn.onclick = function(){
            local.objects.board.removeChild(banner);
        };

        banner.appendChild(removeBtn);
        local.objects.board.appendChild(banner);
    };
    local.board.isColored = function(){
        for (var j=0; j<local.settings.columns; j++){
            for (var i=0; i<local.settings.rows; i++){
                if(
                    !local.space.getElement(i,j).classList.contains('colored') &&
                    !local.space.getElement(i,j).classList.contains('void') &&
                    !local.space.getElement(i,j).classList.contains('pit')
                ){
                    return false;
                }
            }
        }
        return true;
    };

    local.ship = {};
    local.ship.build = function(){
        var ship = document.createElement('div');
        ship.id = 'ship';

        var baseSize = (local.settings.spaceSize-10);
        var lrSize = (baseSize/10)*5;

        ship.style.borderLeftWidth = lrSize+'px';
        ship.style.borderRightWidth = lrSize+'px';
        ship.style.borderTopWidth = baseSize+'px';
        //ship.style.left = Math.round(((local.settings.spaceSize/10)/2)*-1)+'px';
        ship.style.transitionDuration = (local.settings.speed-50)+'ms';
        ship.classList.add(local.state.ship.orientation);

        ship.style.transform = 'rotate('+local.state.ship.deg+'deg)';
        ship.style.webkitTransform = 'rotate('+local.state.ship.deg+'deg)';

        local.objects.ship = ship;
    };
    local.ship.place = function(x,y){
        if(local.objects.ship == null){
            local.ship.build();
        }

        local.space.getElement(x,y).appendChild(local.objects.ship);
        local.state.ship.position = [x,y];

        if(local.goals.colorAll != undefined && local.goals.colorAll == true) {
            if (local.space.getElement(x, y).classList.contains('colored')) {
                local.space.getElement(x, y).classList.remove('colored');
            } else {
                local.space.getElement(x, y).classList.add('colored');
            }
        }

        local.ship.checkState();
    };
    local.ship.isOnFinish = function(){
        return local.space.containsShip(local.settings.finish[0],local.settings.finish[1]);
    };
    local.ship.isOnBelt = function(){
        return local.objects.spaces[local.state.ship.position[0]][local.state.ship.position[1]].classList.contains('belt');
    };
    local.ship.isOnPit = function(){
        return local.objects.spaces[local.state.ship.position[0]][local.state.ship.position[1]].classList.contains('pit');
    };
    local.ship.move = {};
    local.ship.move.back = function () {
        var orientation = local.state.ship.orientation;
        if(orientation == 'left'){
            local.state.ship.orientation = 'right';
        }else if(orientation == 'right'){
            local.state.ship.orientation = 'left';
        }else if(orientation == 'top'){
            local.state.ship.orientation = 'bottom';
        }else{
            local.state.ship.orientation = 'top';
        }
        var move = local.ship.move.forward();
        local.state.ship.orientation = orientation;

        return move;
    };
    local.ship.move.forward = function () {
        return local.ship.move.go();
    };
    local.ship.move.go = function () {
        var currentPosition = local.state.ship.position;
        var newPosition = currentPosition.slice();
        var move = true;
        var css = [];
        var wallCheck = [];

        switch (local.state.ship.orientation) {
            case 'left':
                newPosition[1]--;
                if (newPosition[1] < 0) {
                    consoleLog('Boundary bounce');
                    move = false;
                }else{
                    css = ['left', (local.settings.spaceSize*-1)];
                    wallCheck = ['left', 'right'];
                }

                break;
            case 'right':
                newPosition[1]++;
                if (newPosition[1] < local.settings.columns) {
                    css = ['left', local.settings.spaceSize];
                    wallCheck = ['right', 'left'];
                }else{
                    consoleLog('Boundary bounce');
                    move = false;
                }
                break;
            case 'top':
                newPosition[0]--;
                if (newPosition[0] < 0) {
                    consoleLog('Boundary bounce');
                    move = false;
                }else{
                    css = ['top', (local.settings.spaceSize*-1)];
                    wallCheck = ['top', 'bottom'];
                }
                break;

            case 'bottom':
            default:
                newPosition[0]++;

                if (newPosition[0] < local.settings.rows) {
                    css = ['top', local.settings.spaceSize];
                    wallCheck = ['bottom', 'top'];
                }else{
                    consoleLog('Boundary bounce');
                    move = false;
                }
        }

        if (move) {
            var newSpace = local.objects.spaces[newPosition[0]][newPosition[1]];
            var currentSpace = local.objects.spaces[currentPosition[0]][currentPosition[1]];
            if (currentSpace.classList.contains('wall-'+wallCheck[0]) || newSpace.classList.contains('wall-'+wallCheck[1])) {
                consoleLog('Wall bounce');
                move = false;
            } else {
                local.objects.ship.style[css[0]] = css[1] + 'px';
                setTimeout(function () {
                    local.ship.destroy();
                    local.ship.place(newPosition[0], newPosition[1]);
                }, local.settings.speed - 50);
            }
        }

        if(!move) {
            local.ship.checkState();
        }

        return move;
    };
    local.ship.rotate = {};
    local.ship.rotate.left = function (transform) {
        local.ship.setOrientation(false);

        if(transform != false) {
            local.ship.rotate.transform(false);
        }

        return true;
    };
    local.ship.rotate.right = function (transform) {
        local.ship.setOrientation(true);

        if(transform != false) {
            local.ship.rotate.transform(true);
        }

        return true;
    };
    local.ship.rotate.transform = function (toRight) {
        local.state.ship.deg += toRight? 90 : -90;
        local.objects.ship.style.transform = 'rotate('+local.state.ship.deg+'deg)';
        local.objects.ship.style.webkitTransform = 'rotate('+local.state.ship.deg+'deg)';
    };
    local.ship.setOrientation = function(toRight){
        var index = local.orientations.indexOf(local.state.ship.orientation) + (toRight? -1 : 1);
        index = (index === local.orientations.length)? 0 : index;
        index = (index < 0)? (local.orientations.length-1) : index;

        local.objects.ship.classList.remove(local.state.ship.orientation);
        local.objects.ship.classList.add(local.orientations[index]);
        local.state.ship.orientation = local.orientations[index];
        local.ship.checkState();
    };
    local.ship.destroy = function(){
        local.space.getElement(local.state.ship.position[0], local.state.ship.position[1]).removeChild(local.objects.ship);
        local.objects.ship = null;
    };
    local.ship.checkState = function () {
        var currentState = JSON.parse(JSON.stringify(local.state));
        local.stateList.push(currentState);

        try {
            if (local.ship.isOnBelt()) {
                local.actions.pause();
                setTimeout(function () {
                    var orientation = local.state.ship.orientation;
                    local.state.ship.orientation = local.space.getData(local.state.ship.position[0], local.state.ship.position[1], 'direction');
                    local.ship.move.go();
                    local.state.ship.orientation = orientation;
                    local.actions.play();
                }, 50);
            } else if (local.ship.isOnPit()) {
                local.state.finished = true;
                throw 'Into the pit';
            }else if (local.ship.isOnFinish()) {
                local.state.finished = true;

                if (local.state.programmerActionCount > 0 && local.goals.noExtraActions) {
                    throw 'To many moves!';
                }

                local.board.createBanner('Success!', 'success');
            }else if(local.settings.finish != false && currentState.programmerActionCount == 0 && local.state.running === true){
                if (!local.ship.isOnBelt()) {
                    throw 'Not finished';
                }
            }else if (local.goals.colorAll != undefined && local.goals.colorAll == true && local.board.isColored()){
                local.board.createBanner('Success!', 'success');
            }
        }catch (e) {
            local.board.createBanner('Failure!', 'fail', e);
        }
    }

    local.space = {};
    local.space.build = function(x,y){
        var div = document.createElement("div");
        div.id = local.space.getId.byCoordinates(x,y);
        div.classList.add('space');
        div.style.transitionDuration = (local.settings.speed-50)+'ms';

        if(local.settings.showCoordinates){
            div.innerHTML = x+','+y;
        }

        if(local.objects.spaces[x] == undefined){
            local.objects.spaces[x] = [];
        }

        local.objects.spaces[x][y] = div;
    };
    local.space.getCoordinatesByIndex = function(index){
        var rowIndex = Math.floor(index/local.settings.columns);
        var columnIndex = index-(rowIndex*local.settings.columns);
        return [rowIndex, columnIndex];
    };
    local.space.getId = {};
    local.space.getId.byIndex = function(index){
        var coordinates = local.space.getCoordinatesByIndex(index);
        return local.space.getId.byCoordinates(coordinates[0],coordinates[1]);
    };
    local.space.getId.byCoordinates = function(x,y){
        return 'x'+x+'y'+y;
    };
    local.space.addClass = function(x,y,className){
        local.space.getElement(x,y).classList.add(className);
    };
    local.space.setData = function(x,y,type,val){
        local.space.getElement(x,y).setAttribute('data-'+type, val);
    };
    local.space.getData = function(x,y,type){
        return local.space.getElement(x,y).getAttribute('data-'+type);
    };
    local.space.getElement = function(x,y){
        return local.objects.spaces[x][y] || null;
    };
    local.space.containsShip = function(x,y){
        if(local.settings.finish != false) {
            if (local.settings.finish == null) return false;
            if (local.settings.finish.length != [x, y].length) return false;
        }

        for (var i = 0; i < local.state.ship.position.length; ++i) {
            if (local.state.ship.position[i] !== [x,y][i]) return false;
        }
        return true;
    };

    local.build = function () {
        console.log = self.log;

        local.board.build.fieldGrid();
        local.board.build.fieldObjects();
        local.board.build.goalsDisplay();
        local.board.build.actionBar();

        local.ship.place(local.settings.start[0], local.settings.start[1]);
    };

    local.actions = {};
    local.actions.plan = function(action, addBoardAction) {
        if (local.goals.maxActions != undefined && local.state.programmerActionCount > local.goals.maxActions) {
            local.run();
            local.board.createBanner('Failure!', 'fail', 'Te veel acties ('+local.state.programmerActionCount+' geprogrmeerd, '+local.goals.maxActions+' toegestaan)');
            throw 'To many moves';
            console.clear();
        } else {
            local.state.actions.push(action);

            if (addBoardAction && local.board.hasActions()) {
                local.state.actions.push(local.board.executeActions);
            }
        }

    };
    local.actions.planProgrammerAction = function(name, action, addBoardAction){
        local.state.programmerActionCount++;
        local.actions.plan(function () {
            if(local.goals.allowedFunctions != undefined && local.goals.allowedFunctions.indexOf(name) == -1) {
                local.board.createBanner('Failure!', 'fail', name + ' is niet een toegestane functie');
                local.board.writeToActionBar(name, false);
                throw 'Unauthorised move: ' + name;
            }else {
                local.state.programmerActionCount--;
                var success = action();
                local.board.writeToActionBar(name, success);

                if(local.goals.noFailedActions == true && !success){
                    local.board.createBanner('Failure!', 'fail', 'Er heeft een gefaalde actie plaatsgevonden');
                    throw 'No failed moves allowed';
                }
            }
        }, addBoardAction);
    };
    local.actions.execute = function(){
        if(local.state.actions.length > 0) {
            local.actions.play();
        }
    };

    local.actions.play = function(){
        local.state.nextAction = setTimeout(function () {
            var action = local.state.actions.shift();
            if(local.state.finished === false) {
                action();
                local.actions.execute();
            }
        }, local.settings.speed);
    };
    local.actions.pause = function(){
        clearTimeout(local.state.nextAction);
    };

    var setup = {};
    setup.setFinish = function(x,y){
        local.settings.finish = [x,y];
    };
    setup.setStart = function(x,y,direction){
        local.settings.start = [x,y];
        local.state.ship.orientation = direction;
        local.state.ship.deg = (local.orientations.indexOf(direction)*-90);
    };
    setup.addWall = function(x,y,direction){
        var index = local.settings.walls.findIndex(function (wall) {
            return (wall[0] == x && wall[1] == y);
        });

        if (direction == undefined) {
            direction = local.orientations;
        } else {
            direction = [direction];
        }

        if(index  > -1){
            for (var i=0; i<local.settings.walls[index][2].length; i++) {
                direction.push(local.settings.walls[index][2][i]);
            }
            local.settings.walls[index][2] = direction;
        } else {
            local.settings.walls.push([x,y,direction]);
        }
    };

    setup.addPit = function(x,y){
        local.settings.pits.push([x,y]);
    };

    setup.addSpinner = function(x,y,direction){
        local.settings.spinners.push([x,y,direction]);
    };

    setup.addBelt = function(x,y,direction){
        local.settings.belts.push([x,y,direction]);
    };

    setup.setVoid = function(x,y){
        local.settings.voids.push([x,y]);
        setup.addWall(x,y);
    };

    setup.setColored = function(x,y){
        local.settings.colored.push([x,y]);
    };

    local.run = function(){
        if(local.state.running != true) {
            local.state.orignalProgrammerActionCount = local.state.programmerActionCount;
            local.state.running = true;
            local.actions.execute();
        }
    }

    self.run = function(func) {
        var commentStarted = false;
        var lines = func.toString().split("\n").filter(function (line, index) {
            line = line.trim();

            if(index > 0 && line.length > 1 &&  line.indexOf('//') == -1 && line.indexOf('console.log') == -1){
                if(line.indexOf('/*') == 0 || line.indexOf('*/') > -1){
                    commentStarted = !commentStarted;
                    return false;
                }
                return !commentStarted;
            }
            return false;
        });

        local.state.lines = lines;

        if(local.goals.maxLines != undefined && lines.length > local.goals.maxLines){
            local.board.createBanner('Failure!', 'fail', 'Te veel regels ('+local.goals.maxLines+' toegestaan, '+lines.length+' gebruikt)');
        }else {
            func();
            local.run();
        }
    };

    self.log = function(msg){
        local.actions.plan(function () {
            consoleLog(msg);
        }, false);
    };

    self.rotateLeft = function(){
        local.actions.planProgrammerAction('rotateLeft', local.ship.rotate.left, true);
    };

    self.rotateRight = function(){
        local.actions.planProgrammerAction('rotateRight', local.ship.rotate.right, true);
    };

    self.moveForward = function () {
        local.actions.planProgrammerAction('moveForward', local.ship.move.forward,true);
    };

    self.moveBackward = function () {
        local.actions.planProgrammerAction('moveBackward', local.ship.move.back,true);
    };

    self.wait = function () {
        local.actions.planProgrammerAction('wait', function () { return true; },true);
    };

    self.logLineCount = function(){
        consoleLog(local.state.lines.length);
    };

    self.logActionCount = function(){
        consoleLog(local.state.orignalProgrammerActionCount);
    };

    self.loadCustomLevel = function(w, h, s, data){
        local.objects = {
            container: container,
            board: null,
            ship: null,
            spaces: [],
            spinners: []
        };

        local.settings.belts = [];
        local.settings.walls = [];
        local.settings.spinners = [];
        local.settings.pits = [];

        local.settings.showGoals = false;
        local.settings.rows = h;
        local.settings.columns = w;
        local.settings.spaceSize = s;

        for (var i = 0; i < data.length; i++) {
            if(data[i].type == "start"){
                setup.setStart(data[i].y, data[i].x, data[i].direction);
            }
            else if(data[i].type == "finish"){
                setup.setFinish(data[i].y, data[i].x);
            }
            else if(data[i].type == "belt"){
                setup.addBelt(data[i].y, data[i].x, data[i].direction);
            }
            else if(data[i].type == "pit"){
                setup.addPit(data[i].y, data[i].x);
            }
            else if(data[i].type == "spinner"){
                setup.addSpinner(data[i].y, data[i].x, data[i].direction);
            }
            else if(data[i].type == "wall"){
                setup.addWall(data[i].y, data[i].x, data[i].direction);
            }
        }

        local.build();
    };


    self.loadLevel = function(lvl){
        local.settings.showGoals = true;
        levels['level'+lvl]();
        local.build();
    };


    var levels = {
        'level1': function () {
            local.description = 'Behaal de finish';

            //hoogte
            local.settings.rows = 1;
            //breedte
            local.settings.columns = 8;
            //groote vakjes
            local.settings.spaceSize = 100;

            setup.setStart(0,0, 'right');
            setup.setFinish(0,7);
        },

        'level2': function () {
            local.description = 'Behaal de finish met de volgende criteria:';

            //hoogte
            local.settings.rows = 1;
            //breedte
            local.settings.columns = 8;
            //groote vakjes
            local.settings.spaceSize = 100;

            local.goals.maxLines = 2;
            local.goals.noExtraActions = true;

            setup.setStart(0,0, 'right');
            setup.setFinish(0,7);
        },

        'level3': function () {
            local.description = 'Behaal de finish met de volgende criteria:';

            local.goals.maxLines = 8;
            local.goals.noFailedActions = true;

            //hoogte
            local.settings.rows = 2;
            //breedte
            local.settings.columns = 8;
            //groote vakjes
            local.settings.spaceSize = 100;
            for (var i=0; i<7; i++){
                setup.addWall(1,i,'top');
            }

            setup.setStart(0,0, 'right');
            setup.setFinish(1,0);
        },

        'level4': function () {
            local.description =  'Behaal de finish met de volgende criteria:';

            //hoogte
            local.settings.rows = 7;
            //breedte
            local.settings.columns = 8;
            //groote vakjes
            local.settings.spaceSize = 100;

            local.goals.maxLines = 15;

            for (var i=1; i<8; i++) {
                setup.setVoid(0, i);
            }

            for (var i=0; i<7; i++){
                for (var j=2; j<8; j++) {
                    setup.addWall(j, i, 'top');
                    j++;
                }
            }

            for (var i=1; i<8; i++){
                for (var j=1; j<7; j++) {
                    setup.addWall(j, i, 'top');
                    j++;
                }
            }

            setup.setStart(0,0, 'left');
            setup.setFinish(6,0);
        },

        'level5': function () {
            local.description = 'Behaal de finish met de volgende criteria:';

            //hoogte
            local.settings.rows = 4;
            //breedte
            local.settings.columns = 4;
            //groote vakjes
            local.settings.spaceSize = 150;

            local.goals.allowedFunctions = ['moveBackward', 'wait'];
            local.goals.noExtraActions = true;
            local.goals.maxLines = 8;


            setup.setVoid(1,0);
            setup.setVoid(1,1);
            setup.setVoid(1,2);
            setup.setVoid(2,0);
            setup.setVoid(2,1);
            setup.setVoid(2,2);
            //setup.setVoid(2,2);

            setup.addSpinner(0,0, 'left');
            setup.addSpinner(0,3, 'left');
            setup.addSpinner(3,3, 'left');

            setup.setStart(0,0, 'right');
            setup.setFinish(3,0);
        },

        'level6': function () {

            //hoogte
            local.settings.rows = 4;
            //breedte
            local.settings.columns = 4;
            //groote vakjes
            local.settings.spaceSize = 120;

            local.goals.maxActions = 2;

            setup.addBelt(1,0, 'right');
            setup.addBelt(1,1, 'bottom');
            setup.addBelt(2,1, 'bottom');
            setup.addBelt(3,1, 'right');
            setup.addBelt(3,2, 'right');
            setup.addBelt(3,3, 'top');
            setup.addBelt(2,3, 'left');
            setup.addBelt(2,2, 'top');
            setup.addBelt(1,2, 'right');
            setup.addBelt(1,3, 'top');

            setup.setStart(0,0, 'right');
            setup.setFinish(0,3);
        },



        'level7': function () {

            //hoogte
            local.settings.rows = 2;
            //breedte
            local.settings.columns = 5;
            //groote vakjes
            local.settings.spaceSize = 120;

            setup.addPit(0,1);
            setup.addPit(1,3);

            setup.setStart(0,0, 'right');
            setup.setFinish(0,4);
        },

        'level8': function () {
            local.settings.rows = 9;
            //breedte
            local.settings.columns = 8;

            local.description = 'Behaal de finish met de volgende criteria:';
            local.goals.maxLines = 8;
            local.goals.noFailedActions = true;


            setup.setVoid(1,1);
            setup.setVoid(1,2);
            setup.setVoid(1,3);
            setup.setVoid(1,4);
            setup.setVoid(1,5);

            setup.setVoid(1,6);
            setup.setVoid(2,6);
            setup.setVoid(3,6);
            setup.setVoid(4,6);
            setup.setVoid(5,6);
            setup.setVoid(6,6);
            setup.setVoid(7,6);
            setup.setVoid(8,6);

            setup.setVoid(8,0);
            setup.setVoid(8,1);
            setup.setVoid(8,2);
            setup.setVoid(8,3);
            setup.setVoid(8,4);
            setup.setVoid(8,5);

            setup.setVoid(7,0);
            setup.setVoid(7,1);
            setup.setVoid(7,2);
            setup.setVoid(7,3);
            setup.setVoid(7,4);
            setup.setVoid(7,5);

            setup.setVoid(2,1);
            setup.setVoid(3,1);
            setup.setVoid(4,1);
            setup.setVoid(5,1);

            setup.setVoid(5,2);
            setup.setVoid(5,3);
            setup.setVoid(5,4);

            setup.setVoid(4,4);
            setup.setVoid(3,4);

            setup.addWall(3,3, 'top');
            setup.addWall(3,3, 'left');

            setup.setFinish(3,3);
            setup.setStart(8,7, 'top');
        },

        'level9': function () {
            local.settings.columns = 5;

            local.description = 'Kleur alle velden met de volgende criteria:';

            local.goals.colorAll = true;
            local.goals.maxLines = 15;

            setup.setStart(0,0, 'top');
            for (var i=1; i<=5; i++) {
                setup.setVoid(i, 0);
            }
        },
        'level10': function () {

            local.settings.rows = 5;

            local.description = 'Kleur alle velden met de volgende criteria:';

            local.goals.noExtraActions = true;
            local.goals.noFailedActions = true;
            local.goals.colorAll = true;


            setup.setStart(0,0, 'right');

            setup.addBelt(1,2, 'right');
            setup.addBelt(1,3, 'right');
            setup.addBelt(0,2, 'bottom');
            setup.addBelt(1,4, 'bottom');
            setup.addBelt(2,1, 'left');
            setup.addBelt(3,1, 'top');

            setup.addSpinner(2,4, 'right');
            setup.addSpinner(3,0, 'left');

            setup.setVoid(2,3);
            setup.setVoid(2,2);
            setup.addPit(3,5);

            setup.setColored(0,2);
            setup.setColored(1,2);
            setup.setColored(1,3);
            setup.setColored(1,4);
            setup.setColored(2,4);
            setup.setColored(2,1);
            setup.setColored(2,0);

            setup.addWall(1,3,'top');
            setup.addWall(0,0,'bottom');
            setup.addWall(0,1,'bottom');
            setup.addWall(1,4,'right');
            setup.addWall(4,1,'top');
            setup.addWall(4,2,'top');
            setup.addWall(4,3,'top');
            setup.addWall(4,4,'top');
            setup.addWall(4,3,'top');
            setup.addWall(2,1,'right');
        }
    }
};
