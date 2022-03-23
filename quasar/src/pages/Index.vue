<template>
 <div class="q-pa-md q-gutter-sm">
     <div class="row">
     <q-btn label="Chat Log" color="primary" @click="basic = true" />
     <q-btn label="Playlist" color="primary" @click="fixed = true" />
     </div>

    <div class="column col desktop-only">
        <iframe src="https://www.twitch.tv/embed/reverenddankxlu/chat?parent=trash.rocklosangeles.com&parent=localhost"
            height="750"
            width="100%">
        </iframe>
    </div>
    <div class="column col absolute-full  mobile-only">
        <iframe src="https://www.twitch.tv/embed/reverenddankxlu/chat?parent=trash.rocklosangeles.com?parent=192.168.0.139"
            height="90%"
            width="100%">
        </iframe>
    </div>
    <q-dialog v-model="basic" transition-show="rotate" transition-hide="rotate">
      <q-card>
        <q-card-section>
          <div class="text-h6">Your Permanent Record</div>
        </q-card-section>

        <q-card-section class="q-pt-none">
          <p v-for="n in 15" :key="n">Lorem ipsum dolor sit amet consectetur adipisicing elit. Rerum repellendus sit voluptate voluptas eveniet porro. Rerum blanditiis perferendis totam, ea at omnis vel numquam exercitationem aut, natus minima, porro labore.</p>
        </q-card-section>

      </q-card>
    </q-dialog>

    <q-dialog v-model="fixed">
      <q-card>
        <q-card-section>
          <div class="text-h6">Playlist</div>
        </q-card-section>

        <q-separator />

        <q-card-section style="max-height: 50vh" class="scroll">
          <p v-for="n in 15" :key="n">Lorem ipsum dolor sit amet consectetur adipisicing elit. Rerum repellendus sit voluptate voluptas eveniet porro. Rerum blanditiis perferendis totam, ea at omnis vel numquam exercitationem aut, natus minima, porro labore.</p>
        </q-card-section>

        <q-separator />

      </q-card>
    </q-dialog>

    <q-dialog v-model="seamless" seamless position="bottom">
      <q-card style="width: 350px">

        <q-card-section class="row items-center no-wrap">
          <div>
            <div class="text-weight-bold">Land Shrimp and Long Pork</div>
            <div class="text-grey">The Mormons</div>
          </div>

          <q-space />

         <q-btn
         class="q-mr-sm"
         color="red"
         @click.prevent="audio.isPlaying ? pause(audio) : play(audio)"
         v-for="audio in audios"
         :key="audio.id"
       >
         {{ audio.isPlaying ? "Stop" : "Play" }}
       </q-btn>

        </q-card-section>
      </q-card>
    </q-dialog>
  </div>
</template>

<script>
export default {
  name: 'PageIndex',
  data () {
    return {
      seamless: true,
      basic: false,
      fixed: false,
      audios: [
         {
           id: "mp3",
           file: new Audio(),
           isPlaying: false,
         },
       ],

    }
  },
  methods: {
      play(audio) {
       audio.isPlaying = true;
       audio.file.src = "https://trash.rocklosangeles.com:9595/live.mp3";
       audio.file.play();
     },

     pause(audio) {
       audio.isPlaying = false;
       audio.file.pause();
       audio.file.src =
         "data:audio/wav;base64,UklGRiQAAABXQVZFZm10IBAAAAABAAEAVFYAAFRWAAABAAgAZGF0YQAAAAA=";
     },
  }
}
</script>
