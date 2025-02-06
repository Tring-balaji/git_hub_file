function showname(){
    let name ="Balaji"
    console.log(name)
}
showname()
let paintColor = 'Red'
const paint = (() => {
    return {
        changeColorToBlue: () => {
            paintcolor: 'Blue';
            return paintColor;
        },
        changeColorToGreen: () => {
            paintColor: 'Green';
            return paintColor;
        }
    }
})();

console.log(
    //paint.changeColorToBlue()
    paint.changeColorToGreen()
);
cowsays("moo");
function cowsays(sound){
    console.log(sound);
}
cowsays("moo");