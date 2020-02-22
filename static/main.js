var rec = null;

navigator.mediaDevices.getUserMedia({ audio: true}).then(function(stream) {
    var AudioContext = window.AudioContext || window.webkitAudioContext;
    var audioContext = new AudioContext;
});

function startRecording(button) {
    const input = audioContext.createMediaStreamSource(stream);
    rec = new Recorder(input)
    rec && rec.record();
    button.disabled = true;
    button.nextElementSibling.disabled = false;
    console.log('Recording...');
}

function stopRecording(button) {
    rec && rec.stop();
    button.disabled = true;
    button.previousElementSibling.disabled = false;
    console.log('Stopped recording.');
    
    sendFile();
    
    //rec.clear();
  }

function sendFile() {
    rec && rec.exportWAV(function(blob) {
        console.log(blob);
        fetch("/create", {
            method: "post",
            body: blob
        }).then(async (res) => {
            let fileName = await res.text();
            let shareButton = document.createElement('div')
            shareButton.innerHTML = `<button class='btn btn-primary' onclick='share(${fileName})'>Delen!</button>`
            swal({
                title: 'Gelukt!',
                text: "Klik op de download knop om je bestand te downloaden",
                content: shareButton,
                type: 'success',
                buttons: {
                    cancel: "Sluiten",
                    download: {
                      text: "Downloaden",
                      value: "download",
                    },
                  },
            }).then(async (result) => {
                switch (result) {
                    case "download":
                        window.open(`/static/sounds/${fileName}.mp3`);
                    default:
                        break;
                }
            });
        });
    });
}

function share(sound_id) {
    if(navigator.share) {
        navigator.share({
          title: 'DeelHetMee.social',
          text: 'Bekijk deze nieuwe mededeling!',
          url: `/share/${sound_id}`
        })
    } else {
        window.open(`/share/${sound_id}`)
    }
}