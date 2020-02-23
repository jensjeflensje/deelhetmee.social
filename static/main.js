var rec = null;


function startRecording(button) {
    navigator.mediaDevices.getUserMedia({ audio: true}).then(function(stream) {
        var AudioContext = window.AudioContext || window.webkitAudioContext;
        var audioContext = new AudioContext;
        const input = audioContext.createMediaStreamSource(stream);
        rec = new Recorder(input)
        rec.record();
        button.disabled = true;
        button.nextElementSibling.disabled = false;
        console.log('Recording...');
    });
}

function stopRecording(button) {
    rec.stop();
    button.disabled = true;
    button.previousElementSibling.disabled = false;
    console.log('Stopped recording.');
    
    sendFile();
    
    //rec.clear();
  }

function sendFile() {
    rec && rec.exportWAV(function(blob) {
        console.log(blob);
        var prefix_elem = document.getElementById("prefix_sound");
        var prefix_sound = prefix_elem.options[prefix_elem.selectedIndex].value;
        fetch(`/create/${prefix_sound}`, {
            method: "post",
            body: blob
        }).then(async (res) => {
            let fileName = await res.text();
            let shareButton = document.createElement('div')
            shareButton.innerHTML = `<button class='btn btn-lg btn-primary' onclick='share(${fileName})'>Delen!</button>`
            swal({
                title: 'Gelukt!',
                text: "Het is gelukt! Je kan het bericht gelijk delen, of naar de pagina gaan.",
                content: shareButton,
                type: 'success',
                buttons: {
                    cancel: "Sluiten",
                    watch: {
                      text: "Bekijken",
                      value: "watch",
                    },
                  },
            }).then(async (result) => {
                switch (result) {
                    case "watch":
                        window.open(`/share/${fileName}`);
                    default:
                        break;
                }
            });
        });
    });
}