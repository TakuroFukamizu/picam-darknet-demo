<template>
    <v-container grid-list-md text-xs-center>
        <v-layout row wrap>
            <v-flex xs8>
                <v-progress-circular
                    :size="70"
                    :width="7"
                    v-if="isLoading"
                    color="purple"
                    indeterminate
                    ></v-progress-circular>
                <img :src="imageSrc" v-else>
            </v-flex>
            <v-flex xs4>
                <v-btn color="success" v-on:click="handleClick">Preview</v-btn>
                <br>
                <v-btn color="success" v-on:click="handleDetectClick">Detect</v-btn>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script lang="ts">
// import Vue from 'vue'
import { Component, Prop, Vue } from 'vue-property-decorator';
// import { mapGetters, mapMutations } from 'vuex'
// import { Mutation } from 'vuex-class'

// @Component({
//     computed: {
//         ...mapGetters({ counter: 'current' })
//     },
//     methods: {
//         ...mapMutations(['increment'])
//     }
// })


@Component
export default class Preview extends Vue {
//   @Prop() private value!: number
//   @Mutation('increment') increment!: () => void
    private imageSrc: string = 'http://devraspi02.local:8080/api/v1/get_preview';
    private isLoading: boolean = false;

    private handleClick() {
        this.isLoading = true;
        // const api = "/api/v1/get_preview";
        const api = 'http://devraspi02.local:8080/api/v1/get_preview?mode=base64';
        this.axios.get(api).then((response) => {
            this.isLoading = false;
            console.log(response, typeof(response.data));
            // const file = new Blob([response.data], {type: 'image/jpeg'});
            // const file = new Blob([response.data], {type: response.headers['content-type']});
            // console.log(file);
            // this.imageSrc = URL.createObjectURL(file);
            this.imageSrc = 'data:image/jpg;base64,' + response.data;
        });
    }

    getItem() {
        return true;
    }

    private handleDetectClick() {
        this.isLoading = true;
        // const api = "/api/v1/get_preview";
        const api = 'http://devraspi02.local:8080/api/v1/detect_people';
        this.axios.get(api).then((response) => {
            this.isLoading = false;
            console.log(response, typeof(response.data));
            this.imageSrc = 'data:image/jpg;base64,' + response.data['result_image'];
        });
    }

    
}
</script>

<style scoped>
img {
    width:auto;
    height:auto;
    max-width:100%;
    max-height:100%;
}
</style>

