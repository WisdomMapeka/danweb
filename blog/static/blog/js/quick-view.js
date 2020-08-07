
// // // QUICK VIEW AN IMAGE
// function Enlarge_img(value){
    
//    var close_class = "close_img";
//    close_class+=value;
//    var img_figure = document.getElementsByClassName("img-figure-"+value)[0];
//    var img = document.getElementsByClassName("images-"+value)[0];
//    var div = document.getElementById("div-for-enlarged-img");
//    var close = document.createElement("div");

        
//       close.innerHTML = "close";
//       close.style.position = "absolute";
//       close.style.top = "10px";
//       close.style.right = "10px";
//       close.style.paddingRight = "20px";
//       close.style.paddingLeft  = "20px";
//       close.style.paddingTop  = "10px";
//       close.style.paddingBottom = "10px";
//       close.style.backgroundColor = "red";
//       close.className = close_class;
//       close.addEventListener("click", function() {Close(value, close_class)});



//        div.appendChild(img);
//        div.appendChild(close);
//        div.style.position = "absolute";
//        div.style.width = "80%";
//        div.style.left = "10%";
//        img.style.width = "100%";
//        div.style.zIndex = "100";
     
// }

// function Close(value, close_class){
//    console.log("Yes");
//    var img_figure = document.getElementsByClassName("img-figure-"+value)[0];
//     var img = document.getElementsByClassName("images-"+value)[0];
//     var div = document.getElementById("div-for-enlarged-img");
//     var close = document.getElementsByClassName(close_class)[0];
//    if (div.style.position == "absolute") {
//        div.style.position = "unset";
//        div.removeChild(img);
//        img_figure.prepend(img);

//        close.style.display = "none";

//    }
// }
























// function Enlarge_img(value){
//    var close = document.getElementById('close-img-'+value);
//    var product_container = document.getElementById('product-img-container-'+value);
//    var img = document.getElementById('product-img-'+value);
//    var hide_items = document.getElementsByClassName('hide-on-enlarge-'+value);

//     $(document).ready(function(){
//         $("#product-container-"+value).click(
//             function(){
//                 $("#product-container-"+value).css("width", "60%");
//                 $("#product-container-"+value).css("position", "absolute");
//                 $("#product-container-"+value).css("right", "21%");
//                 $("#product-container-"+value).css("top", "10%");
//                 $("#close-img-"+value).css("display", "block");
//                 $("#close-img-"+value).css("position", "absolute");
//                 $("#close-img-"+value).css("top", "3px");
//                 $("#close-img-"+value).css("right", "5px");

//             })

//         $("#close-img-"+value).click(
//             function(){
//                 $("#product-container-"+value).css("width", "300px");
//                 $("#product-container-"+value).css("position", "unset");
//                 $("#product-container-"+value).css("right", "unset");
//                 $("#product-container-"+value).css("top", "unset");
//                 $("#close-img-"+value).css("display", "none");
            
//             })
//     })
// }






