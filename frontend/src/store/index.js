import { createStore } from "vuex";

export default createStore({
    state(){
        return {
            user: {
                token: null,
                roles: []
            }
        }
    },
    mutations: {
        setUser(state, value){
            localStorage.setItem("user", JSON.stringify(value));
            state.user = value;
        }
    },
    getters: {
        getRoles(userstate){
            return userstate.user["roles"];
        },
        getToken(userstate){
            return userstate.user["token"];
        }
    }
});