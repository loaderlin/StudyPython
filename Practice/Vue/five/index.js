var app = new Vue({
    el: '#app',
    data: {
        list: [
            { id: 1, name: 'iPhone 7', price: 6188, count: 1},
            { id: 2, name: 'iPhone Pro', price: 5888, count: 1},
            { id: 3, name: 'MacBook pro', price: 21488, count: 1},
            { id: 4, name: 'iPhone XS ', price: 10999, count: 1},
            { id: 5, name: 'iPhone XS Max', price: 20999, count: 1}
        ],
        checked: false,
        checkList: [],
    },
    computed: {
        totalPrice: function() {
            var total = 0;
            var goodsList = this.checkList || this.list;
            for (var i=0; i < goodsList.length; i++){
                var item = this.list[this.checkList[i]];
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
        },
        checkAll: function() {
            if(this.checked) {
                this.checkList = [];
                this.checked = false;
            }else {
                for (var i=0; i < this.list.length; i++){
                    this.checkList.push(i);
                }
                this.checked = true;
            }
        },
    }
});