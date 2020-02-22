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



window.onresize = () => {
    const mq = window.matchMedia( "(min-width: 960px)" );

    if (mq.matches) {
        document.getElementById("share-btn").style.display = "none";
    } else {
        document.getElementById("share-btn").style.display = "block";
    }
}