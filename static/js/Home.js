
const colors = ["#2E81FF", "#00E8DA", "#FF1C6D", "#FF6D1C", "#DFFF1C"];
const methods = [
  "Curve Fitting",
  "Surface Fitting",
  "Numerical Calculus",
  "Differential Eqs.",
  "Systems of Eqs",
];

const tooltips = [
  "This section involves methods that tackle interpolation and curve fitting problems. To know more about any of the methods, check the PDF document by clicking on the book icon that's within the method's page.",
  "This section involves methods that tackle interpolation and surface fitting problems. To know more about any of the methods, check the PDF document by clicking on the book icon that's within the method's page.",
  "This section includes methods that solve differentiation, integration & optimization problems. To know more about any of the methods, check the PDF document by clicking on the book icon that's within the method's page.",
  "This section involves methods that numerically solve ordinary and partial differential equations. To know more about any of the methods, check the PDF document by clicking on the book icon that's within the method's page.",
  "This section involves methods that help solve linear and nonlinear systems of equations as well as the Eigenvalue problem. To know more about any of the methods, check the PDF document by clicking on the book icon that's within the method's page.",
];

const M = [
  [
    "Least Squares Regression: LMA & The Normal Equation",
    "Polynomial  & Bézier Interpolation: Lagrange & Newton’s Method",
    "Spline Interpolation: Linear, Quadratic & Cubic Polynomials",
    "Least Absolute Deviations: Iteratively Reweighted Least Squares",
  ],
  [
    "Surface Fitting: Ordinary Least Squares",
    "Surface Interpolation: Bivariate Polynomials With Zero Residuals",
    "Bilinear Interpolation (Coming Soon)",
    "",
  ],
  [
    "Differentiation: Finite Differences & Richardson Extrapolation",
    "Integration: Newton-Cotes, Romberg’s Rule & Gauss Quadrature",
    "Optimization: Gradient Descent & Newton’s Method (Coming Soon)",
    "",
  ],
  [
    "Ordinary Differential Equations: Runge-Kutta Methods",
    "Ordinary Differential Equations: Euler & Huen Methods",
    "Ordinary Differential Equations: Adams-Bashforth Methods",
    "Partial Differential Equations: Finite Differences",
  ],
  [
    "Linear Systems of Equations: Gauss-Seidel and SOR",
    "Nonlinear Systems of Equations: Fixed Point Iteration & Newton’s Method",
    "The Eigenvalue Problem: Power Method With Deflation",
    "",
  ],
];

const A = [
  [
    "/LeastSquareReg",
    "/PolynomialInterpolation",
    "/SplineInterpolation",
    "/LeastAbsoluteErrors",
  ],
  ["/SurfaceFitting", "/SurfaceInterpolation", "/BI", "/home"],
  ["/Differentiation", "/Integration", "/GradientDescent", "/home"],
  ["/ODERK", "/ODEEH", "/ODEPC", "/PDE"],
  ["/LinearSystem", "/NonlinearSystem", "/EigenvalueProblem", "/home"],
];

document.getElementById("Uni").addEventListener("mouseenter", () => {
  document.getElementById("pyro").style.display = "block";
  document.getElementById('Uni').style.cursor="none";
});

document.getElementById("Uni").addEventListener("mouseout", () => {
  document.getElementById("pyro").style.display = "none";
});

const flatA = A.flat();
allAnchors = flatA.filter((stringo) => {
  return stringo != "/home";
});

const allMethods = [
  "Least Squares Regression: LMA & The Normal Equation",
  "Polynomial  & Bézier Interpolation: Lagrange & Newton’s Method",
  "Spline Interpolation: Linear, Quadratic & Cubic Polynomials",
  "Least Absolute Deviations: Iteratively Reweighted Least Squares",

  "Surface Fitting: Ordinary Least Squares",
  "Surface Interpolation: Bivariate Polynomials With Zero Residuals",
  "Bilinear Interpolation",

  "Differentiation: Finite Differences & Richardson Extrapolation",
  "Integration: Newton-Cotes, Romberg’s Rule & Gauss Quadrature",
  "Optimization: Gradient Descent & Newton’s Method",

  "Ordinary Differential Equations: Runge-Kutta Methods",
  "Ordinary Differential Equations: Euler & Huen Methods",
  "Ordinary Differential Equations: Adams-Bashforth Methods",
  "Partial Differential Equations: Finite Differences",

  "Linear Systems of Equations: Gauss-Seidel and SOR",
  "Nonlinear Systems of Equations: Fixed Point Iteration & Newton’s Method",
  "The Eigenvalue Problem: Power Method With Deflation",
];

document.getElementById("love").addEventListener("mouseenter", function () {
  var R = document.querySelector(":root");
  var color = getComputedStyle(R).getPropertyValue("--primary-color");
  i = colors.indexOf(color);
  document.getElementById("love").style.cursor =
    "url(" + "'/static/favicon/GG" + i + ".svg'), default";
  document.getElementById("love").innerHTML = "&nbsp;&nbsp;&nbsp&nbsp;&nbsp;";
  document.getElementById("Cairo").innerHTML =
    "You rediscovered <span>Mathemati</span>, position the heart carefully and click <span> <3 </span>.";
  document.getElementById("Cairo").style.fontWeight = 500;
  setTimeout(()=>{window.scrollTo({ top: 100, behavior: 'smooth' }) },1000);
  
});
document.getElementById("love").addEventListener("mouseout", function () {
  document.getElementById("love").innerHTML = "o";
  document.getElementById("Cairo").innerHTML =
    "Copyright &copy; 2021 <span>Cairo University</span>, &nbsp;  All Rights Reserved.";
});

window.onload = () => {
  let Q = getRandomInt(0, 5);
  var R = document.querySelector(":root");
  R.style.setProperty("--primary-color", colors[Q]);
  document
    .querySelectorAll(".navBar nav ul li a")
    .forEach((link) => (link.style.color = "white"));
  document.getElementById(IDs[Q]).firstChild.style.color = colors[Q];
  document.getElementById("family").innerHTML = methods[Q];
  document.getElementById("tooltip").innerHTML = tooltips[Q];
  for (let j = 0; j <= 3; j++) {
    let anchor = document.getElementById("methods").childNodes[j].childNodes[0];
    anchor.innerHTML = M[Q][j];
    anchor.href = A[Q][j];
  }

  if (M[Q][3] == "") {
    document.getElementById("methods_id").style.display = "none";
    document.getElementById("Qmark").style.top = "8.7rem";
  } else {
    document.getElementById("methods_id").style.display = "block";
    document.getElementById("Qmark").style.top = "11.7rem";
  }

  favicon = "/static/favicon/M" + Q + ".png";
  document.getElementsByTagName("link")[2].href = favicon;
};

document.getElementById("leftArrow").addEventListener("click", function () {
  toTheLeft();
});

document.getElementById("rightArrow").addEventListener("click", function () {
  toTheRight();
});

const IDs = ["Curve", "Surface", "Calculus", "Differential", "Systems"];
for (let k = 0; k < IDs.length; k++) {
  document.getElementById(IDs[k]).addEventListener("click", function () {
    var R = document.querySelector(":root");
    R.style.setProperty("--primary-color", colors[k]);
    document
      .querySelectorAll(".navBar nav ul li a")
      .forEach((link) => (link.style.color = "white"));
    document.getElementById(IDs[k]).firstChild.style.color = colors[k];

    document.getElementById("family").innerHTML = methods[k];

    for (let j = 0; j <= 3; j++) {
      let anchor =
        document.getElementById("methods").childNodes[j].childNodes[0];
      anchor.innerHTML = M[k][j];
      anchor.href = A[k][j];
    }

    if (M[k][3] == "") {
      document.getElementById("methods_id").style.display = "none";
      document.getElementById("Qmark").style.top = "8.7rem";
    } else {
      document.getElementById("methods_id").style.display = "block";
      document.getElementById("Qmark").style.top = "11.7rem";
    }
  });
}

document.body.addEventListener("keydown", function (event) {
  const key = event.key;
  var myElement = document.getElementById("S");
  if (myElement !== document.activeElement) {
    switch (key) {
      case "ArrowLeft":
        toTheLeft();
        break;
      case "ArrowRight":
        toTheRight();
        break;
    }
  }
});

function toTheRight() {
  var R = document.querySelector(":root");
  var color = getComputedStyle(R).getPropertyValue("--primary-color");
  i = colors.indexOf(color);

  if (i != 4) {
    R.style.setProperty("--primary-color", colors[i + 1]);
    document.getElementById("family").innerHTML = methods[i + 1];
    document
      .querySelectorAll(".navBar nav ul li a")
      .forEach((link) => (link.style.color = "white"));
    document.getElementById(IDs[i + 1]).firstChild.style.color = colors[i + 1];
    document.getElementById("tooltip").innerHTML = tooltips[i + 1];

    let Q = i + 1;
    favicon = "/static/favicon/M" + Q + ".png";
    document.getElementsByTagName("link")[2].href = favicon;
    document.getElementById("love").style.cursor =
      "url(/static/favicon/GG" + Q + ")";

    for (let j = 0; j <= 3; j++) {
      let anchor =
        document.getElementById("methods").childNodes[j].childNodes[0];
      anchor.innerHTML = M[i + 1][j];
      anchor.href = A[i + 1][j];
    }

    if (M[i + 1][3] == "") {
      document.getElementById("methods_id").style.display = "none";
      document.getElementById("Qmark").style.top = "8.7rem";
    } else {
      document.getElementById("methods_id").style.display = "block";
      document.getElementById("Qmark").style.top = "11.7rem";
    }
  } else {
    R.style.setProperty("--primary-color", colors[0]);
    document.getElementById("family").innerHTML = methods[0];
    document
      .querySelectorAll(".navBar nav ul li a")
      .forEach((link) => (link.style.color = "white"));
    document.getElementById(IDs[0]).firstChild.style.color = colors[0];
    document.getElementById("tooltip").innerHTML = tooltips[0];

    favicon = "/static/favicon/M" + 0 + ".png";
    document.getElementsByTagName("link")[2].href = favicon;
    document.getElementById("love").style.cursor =
      "url(/static/favicon/GG" + 0 + ")";

    for (let j = 0; j <= 3; j++) {
      let anchor =
        document.getElementById("methods").childNodes[j].childNodes[0];
      anchor.innerHTML = M[0][j];
      anchor.href = A[0][j];
    }

    if (M[0][3] == "") {
      document.getElementById("methods_id").style.display = "none";
      document.getElementById("Qmark").style.top = "8.7rem";
    } else {
      document.getElementById("methods_id").style.display = "block";
      document.getElementById("Qmark").style.top = "11.7rem";
    }
  }
}

function toTheLeft() {
  var R = document.querySelector(":root");
  var color = getComputedStyle(R).getPropertyValue("--primary-color");
  i = colors.indexOf(color);
  if (i != 0 && i != -1) {
    R.style.setProperty("--primary-color", colors[i - 1]);
    document
      .querySelectorAll(".navBar nav ul li a")
      .forEach((link) => (link.style.color = "white"));
    document.getElementById(IDs[i - 1]).firstChild.style.color = colors[i - 1];
    document.getElementById("family").innerHTML = methods[i - 1];
    document.getElementById("tooltip").innerHTML = tooltips[i - 1];
    let Q = i - 1;
    favicon = "/static/favicon/M" + Q + ".png";
    document.getElementsByTagName("link")[2].href = favicon;
    document.getElementById("love").style.cursor =
      "url('/static/favicon/GG" + Q + "')";
    for (let j = 0; j <= 3; j++) {
      let anchor =
        document.getElementById("methods").childNodes[j].childNodes[0];
      anchor.innerHTML = M[i - 1][j];
      anchor.href = A[i - 1][j];
    }
    if (M[i - 1][3] == "") {
      document.getElementById("methods_id").style.display = "none";
      document.getElementById("Qmark").style.top = "8.7rem";
    } else {
      document.getElementById("methods_id").style.display = "block";
      document.getElementById("Qmark").style.top = "11.7rem";
    }
  } else {
    R.style.setProperty("--primary-color", colors[4]);
    document.getElementById("family").innerHTML = methods[4];
    document
      .querySelectorAll(".navBar nav ul li a")
      .forEach((link) => (link.style.color = "white"));
    document.getElementById(IDs[4]).firstChild.style.color = colors[4];
    document.getElementById("tooltip").innerHTML = tooltips[4];
    document.getElementById("love").style.cursor =
      "url('/static/favicon/GG" + 4 + "')";

    favicon = "/static/favicon/M" + 4 + ".png";
    document.getElementsByTagName("link")[2].href = favicon;

    for (let j = 0; j <= 3; j++) {
      let anchor =
        document.getElementById("methods").childNodes[j].childNodes[0];
      anchor.innerHTML = M[4][j];
      anchor.href = A[4][j];
    }

    if (M[4][3] == "") {
      document.getElementById("methods_id").style.display = "none";
      document.getElementById("Qmark").style.top = "8.7rem";
    } else {
      document.getElementById("methods_id").style.display = "block";
      document.getElementById("Qmark").style.top = "11.7rem";
    }
  }
}

var searchedIndex = -1;
document.getElementById("S").addEventListener("input", function (event) {
  let searchWord = document.getElementById("S").value;

  if (searchWord.length > 0) {
    for (let c = 0; c < allMethods.length; c++) {
      for (let m = 0; m <= allMethods[c].length; m++) {
        if (
          allMethods[c].charAt(m).toUpperCase() !== allMethods[c].charAt(m) ||
          allMethods[c].charAt(m).toUpperCase() == "M" ||
          allMethods[c].charAt(m).toUpperCase() == "&"
        )
          continue;
        let test = allMethods[c].slice(m, m + searchWord.length).toLowerCase();
        let input = searchWord.toLowerCase();
        if (test === input) {
          document
            .getElementById("searchBox")
            .setAttribute(
              "placeholder",
              searchWord + allMethods[c].slice(m + searchWord.length)
            );
          var found = 1;
          break;
        }
      }
      if (found == 1) {
        searchedIndex = c;
        break;
      }
    }
    if (!found) {
      document.getElementById("searchBox").setAttribute("placeholder", "");
    }
  } else {
    document.getElementById("searchBox").setAttribute("placeholder", "");
  }
});

document.getElementById("S").addEventListener("keydown", function (event) {
  const key = event.key;
  var myElement = document.getElementById("Search");

  if (key == "Enter" || key == "ArrowDown" || key == "Tab") {
    if (key == "Tab") {
      event.preventDefault();
    }
    document.getElementById("S").value = document
      .getElementById("searchBox")
      .getAttribute("placeholder");
    if (key == "Enter" && searchedIndex != -1) {
      event.preventDefault();

      if(searchedIndex !== -1)
      {
        //fetch(window.location.origin + allAnchors[searchedIndex]);
          window.location.href = window.location.origin + allAnchors[searchedIndex] ;
      }
    }
  }
});

// document.getElementById('searchIcon').addEventListener( 'click', ()=>{

// if(searchedIndex !== -1)
// {
//   document.getElementById("searchIcon").action = allAnchors[searchedIndex];
// }

// });

document.getElementById("Qmark").addEventListener("click", function () {
  if (document.getElementById("tooltip").style.display == "none") {
    document.getElementById("tooltip").style.display = "block";
    document.getElementById("Qmark").style.transform = "scale(0.9)";
  } else {
    document.getElementById("tooltip").style.display = "none";
    document.getElementById("Qmark").style.transform = "scale(0.8)";
  }
});




function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min) + min); //The maximum is exclusive and the minimum is inclusive
}
