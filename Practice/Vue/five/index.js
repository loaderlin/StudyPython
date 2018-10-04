var app = new Vue({
    el: '#app',
    data: {
        list: [
            { id: 1, name: 'iPhone 7', price: 6188, count: 1},
            { id: 1, name: 'iPhone Pro', price: 5888, count: 1},
            { id: 1, name: 'MacBook pro', price: 21488, count: 1},
            { id: 1, name: 'iPhone XS ', price: 10999, count: 1},
            { id: 1, name: 'iPhone XS Max', price: 20999, count: 1}
        ]
    },
    computed: {
        totalPrice: function() {
            var total = 0;
            for (var i=0; i < this.list.length; i++){
                var item = this.list[i];
                total += item.price * item.count;
            }
            return total.toString().replace(/\B(?=(\d{3})+$)/g, ',');
        }
    },
    methods: {
        handleReduce: function (index) {
            if (this.list[index].count === 1) return ;
            this.list[index].count--;
        },
        handleAdd: function (index) {
            this.list[index].count++;
        },
        handleRemove: function (index) {
            this.list.splice(index, 1);
        }
    }
})