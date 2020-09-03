function sendToPython() {
    var { PythonShell } = require('python-shell');

    let options = {
        mode: 'text',
        args: [input.value]
    };
    
    PythonShell.run('brainyPython/calc.py', options, function (err, results){
        if (err) throw err;
        console.log('results: ', results);
        result.textContent = results[0]
    });
}    

btn.addEventListener('click', () => {
        sendToPython();
});

btn.dispatchEvent(new Event('click'));
 