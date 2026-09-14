// ============================================================
// SafePath AI - Final Frontend
// A -> V
// Wheelchair = stair roads blocked
// Women Safety = CCTV roads preferred
// ============================================================


// ============================================================
// NODES
// ============================================================

const NODES = {

    A: { x: 70,  y: 220, name: "Main Gate" },
    B: { x: 180, y: 160, name: "Library" },
    C: { x: 300, y: 140, name: "School" },
    D: { x: 180, y: 310, name: "Parking" },

    E: { x: 360, y: 250, name: "Campus" },
    F: { x: 480, y: 150, name: "Hospital" },
    G: { x: 600, y: 220, name: "Mall" },

    H: { x: 430, y: 70, name: "Metro Station" },
    I: { x: 300, y: 380, name: "Bus Stop" },
    J: { x: 450, y: 320, name: "Cafeteria" },

    K: { x: 560, y: 300, name: "Admin Block" },
    L: { x: 700, y: 150, name: "Auditorium" },

    M: { x: 570, y: 430, name: "Playground" },
    N: { x: 680, y: 380, name: "Hostel" },
    O: { x: 700, y: 300, name: "Sports Complex" },

    P: { x: 790, y: 300, name: "Main Road" },
    Q: { x: 820, y: 190, name: "Market" },

    R: { x: 700, y: 480, name: "Pharmacy" },
    S: { x: 800, y: 430, name: "ATM" },
    T: { x: 880, y: 370, name: "Police Help Desk" },

    U: { x: 880, y: 500, name: "Garden" },
    V: { x: 790, y: 560, name: "Parking 2" }

};


// ============================================================
// GRAPH EDGES
// ============================================================

const EDGES = [

    ["A", "B"],
    ["A", "D"],

    ["B", "C"],
    ["B", "E"],

    ["C", "F"],
    ["C", "H"],

    ["D", "E"],
    ["D", "I"],

    ["E", "F"],
    ["E", "G"],
    ["E", "J"],

    ["F", "G"],
    ["F", "K"],

    ["G", "L"],

    ["H", "K"],
    ["H", "M"],

    ["I", "J"],
    ["I", "N"],

    ["J", "K"],
    ["J", "O"],

    ["K", "L"],
    ["K", "P"],

    ["L", "Q"],

    ["M", "N"],
    ["M", "R"],

    ["N", "O"],
    ["N", "S"],

    ["O", "P"],
    ["O", "T"],

    ["P", "Q"],
    ["P", "U"],

    ["Q", "V"],

    ["R", "S"],

    ["S", "T"],

    ["T", "U"],

    ["U", "V"]

];


// ============================================================
// EXACT STAIR EDGES
// ============================================================

const STAIR_EDGES = new Set([

    "C-F",
    "D-I",
    "F-K",
    "K-L"

]);


function edgeKey(a, b) {

    const forward = `${a}-${b}`;

    const reverse = `${b}-${a}`;

    if (STAIR_EDGES.has(forward)) {
        return forward;
    }

    if (STAIR_EDGES.has(reverse)) {
        return reverse;
    }

    return forward;
}


function isStairEdge(a, b) {

    return STAIR_EDGES.has(
        edgeKey(a, b)
    );
}


// ============================================================
// STATE
// ============================================================

let mode = "normal";

let searching = false;

let currentData = null;


// ============================================================
// DOM
// ============================================================

const startSelect =
    document.getElementById("start");

const goalSelect =
    document.getElementById("goal");

const roadLayer =
    document.getElementById("roadLayer");

const landmarkLayer =
    document.getElementById("landmarkLayer");

const nodeLayer =
    document.getElementById("nodeLayer");

const explorationLayer =
    document.getElementById("explorationLayer");


// ============================================================
// INIT
// ============================================================

document.addEventListener(
    "DOMContentLoaded",
    () => {

        populateDropdowns();

        drawRoads();

        drawLandmarks();

        drawNodes();

        resetDemo();

    }
);


// ============================================================
// DROPDOWNS
// ============================================================

function populateDropdowns() {

    startSelect.innerHTML = "";

    goalSelect.innerHTML = "";


    Object.keys(NODES).forEach(
        id => {

            const option1 =
                document.createElement("option");

            option1.value = id;

            option1.textContent =
                `${id} — ${NODES[id].name}`;

            startSelect.appendChild(
                option1
            );


            const option2 =
                document.createElement("option");

            option2.value = id;

            option2.textContent =
                `${id} — ${NODES[id].name}`;

            goalSelect.appendChild(
                option2
            );

        }
    );


    startSelect.value = "A";

    goalSelect.value = "V";
}


// ============================================================
// ROADS
// ============================================================

function drawRoads() {

    roadLayer.innerHTML = "";


    EDGES.forEach(
        ([a, b]) => {

            const p1 = NODES[a];

            const p2 = NODES[b];


            const line =
                document.createElementNS(
                    "http://www.w3.org/2000/svg",
                    "line"
                );


            line.setAttribute(
                "x1",
                p1.x
            );

            line.setAttribute(
                "y1",
                p1.y
            );

            line.setAttribute(
                "x2",
                p2.x
            );

            line.setAttribute(
                "y2",
                p2.y
            );


            line.classList.add(
                "road"
            );


            line.dataset.a = a;

            line.dataset.b = b;


            if (isStairEdge(a, b)) {

                line.classList.add(
                    "stair-road"
                );

            }


            roadLayer.appendChild(
                line
            );

        }
    );
}


// ============================================================
// LANDMARKS
// ============================================================

function addLandmark(
    x,
    y,
    icon,
    label
) {

    const iconText =
        document.createElementNS(
            "http://www.w3.org/2000/svg",
            "text"
        );


    iconText.setAttribute(
        "x",
        x
    );

    iconText.setAttribute(
        "y",
        y
    );


    iconText.classList.add(
        "landmark"
    );


    iconText.textContent =
        icon;


    landmarkLayer.appendChild(
        iconText
    );


    const labelText =
        document.createElementNS(
            "http://www.w3.org/2000/svg",
            "text"
        );


    labelText.setAttribute(
        "x",
        x
    );

    labelText.setAttribute(
        "y",
        y + 18
    );


    labelText.classList.add(
        "landmark-label"
    );


    labelText.textContent =
        label.toUpperCase();


    landmarkLayer.appendChild(
        labelText
    );
}


function addFeature(
    x,
    y,
    icon,
    label
) {

    const text =
        document.createElementNS(
            "http://www.w3.org/2000/svg",
            "text"
        );


    text.setAttribute(
        "x",
        x
    );

    text.setAttribute(
        "y",
        y
    );


    text.classList.add(
        "feature-icon"
    );


    text.textContent =
        icon;


    landmarkLayer.appendChild(
        text
    );


    const labelText =
        document.createElementNS(
            "http://www.w3.org/2000/svg",
            "text"
        );


    labelText.setAttribute(
        "x",
        x
    );

    labelText.setAttribute(
        "y",
        y + 13
    );


    labelText.classList.add(
        "feature-label"
    );


    labelText.textContent =
        label;


    landmarkLayer.appendChild(
        labelText
    );
}


function midpoint(a, b) {

    return {

        x:
            (NODES[a].x +
             NODES[b].x) / 2,

        y:
            (NODES[a].y +
             NODES[b].y) / 2

    };
}


function drawLandmarks() {

    landmarkLayer.innerHTML = "";


    // -------------------------
    // Main landmarks
    // -------------------------

    addLandmark(
        180,
        115,
        "📚",
        "Library"
    );


    addLandmark(
        300,
        95,
        "🏫",
        "School"
    );


    addLandmark(
        480,
        105,
        "🏥",
        "Hospital"
    );


    addLandmark(
        430,
        38,
        "🚇",
        "Metro"
    );


    addLandmark(
        600,
        180,
        "🛍️",
        "Mall"
    );


    addLandmark(
        880,
        330,
        "👮",
        "Police"
    );


    // -------------------------
    // CCTV
    // -------------------------

    addFeature(
        350,
        115,
        "📹",
        "CCTV"
    );


    addFeature(
        745,
        270,
        "📹",
        "CCTV"
    );


    // -------------------------
    // Ramps
    // -------------------------

    addFeature(
        330,
        225,
        "♿",
        "RAMP"
    );


    addFeature(
        745,
        285,
        "♿",
        "RAMP"
    );


    // =====================================================
    // STAIR ICONS - EXACTLY ON STAIR ROADS
    // =====================================================

    const stairLocations = [

        ["C", "F"],
        ["D", "I"],
        ["F", "K"],
        ["K", "L"]

    ];


    stairLocations.forEach(
        ([a, b]) => {

            const p =
                midpoint(a, b);


            addFeature(
                p.x,
                p.y,
                "🪜",
                "STAIRS"
            );

        }
    );


    // -------------------------
    // Street lights
    // -------------------------

    addFeature(
        220,
        120,
        "💡",
        "LIGHT"
    );


    addFeature(
        660,
        410,
        "💡",
        "LIGHT"
    );
}


// ============================================================
// NODES
// ============================================================

function drawNodes() {

    nodeLayer.innerHTML = "";


    Object.entries(NODES).forEach(
        ([id, node]) => {

            const group =
                document.createElementNS(
                    "http://www.w3.org/2000/svg",
                    "g"
                );


            group.id =
                `node-${id}`;


            const circle =
                document.createElementNS(
                    "http://www.w3.org/2000/svg",
                    "circle"
                );


            circle.setAttribute(
                "cx",
                node.x
            );

            circle.setAttribute(
                "cy",
                node.y
            );

            circle.setAttribute(
                "r",
                21
            );


            circle.classList.add(
                "map-node-circle"
            );


            const text =
                document.createElementNS(
                    "http://www.w3.org/2000/svg",
                    "text"
                );


            text.setAttribute(
                "x",
                node.x
            );

            text.setAttribute(
                "y",
                node.y
            );


            text.classList.add(
                "map-node-text"
            );


            text.textContent =
                id;


            const label =
                document.createElementNS(
                    "http://www.w3.org/2000/svg",
                    "text"
                );


            label.setAttribute(
                "x",
                node.x
            );

            label.setAttribute(
                "y",
                node.y + 34
            );


            label.classList.add(
                "map-node-label"
            );


            label.textContent =
                node.name;


            group.appendChild(
                circle
            );

            group.appendChild(
                text
            );

            group.appendChild(
                label
            );


            nodeLayer.appendChild(
                group
            );

        }
    );
}


// ============================================================
// MODE
// ============================================================

function selectMode(newMode) {

    if (searching) {
        return;
    }


    mode = newMode;


    document
        .querySelectorAll(".mode-btn")
        .forEach(
            btn =>
                btn.classList.remove(
                    "active"
                )
        );


    if (mode === "normal") {

        document
            .getElementById(
                "normalMode"
            )
            .classList.add(
                "active"
            );

    }


    if (mode === "wheelchair") {

        document
            .getElementById(
                "wheelchairMode"
            )
            .classList.add(
                "active"
            );

    }


    if (mode === "women") {

        document
            .getElementById(
                "womenMode"
            )
            .classList.add(
                "active"
            );

    }


    resetDemo();

    applyModeRoadStyle();
}


// ============================================================
// MODE ROAD VISUAL
// ============================================================

function applyModeRoadStyle() {

    document
        .querySelectorAll(".stair-road")
        .forEach(
            road => {

                road.classList.remove(
                    "wheelchair-blocked"
                );


                if (mode === "wheelchair") {

                    road.classList.add(
                        "wheelchair-blocked"
                    );

                }

            }
        );
}


// ============================================================
// RESET
// ============================================================

function resetDemo() {

    searching = false;

    currentData = null;


    document.getElementById(
        "dijkstraCounter"
    ).textContent = "0";


    document.getElementById(
        "astarCounter"
    ).textContent = "0";


    document.getElementById(
        "dijkstraDistance"
    ).textContent = "—";


    document.getElementById(
        "astarDistance"
    ).textContent = "—";


    document.getElementById(
        "dijkstraCost"
    ).textContent = "—";


    document.getElementById(
        "astarCost"
    ).textContent = "—";


    document.getElementById(
        "dijkstraRoute"
    ).textContent = "—";


    document.getElementById(
        "astarRoute"
    ).textContent = "—";


    document.getElementById(
        "shortestText"
    ).textContent = "Cost: —";


    document.getElementById(
        "safestText"
    ).textContent = "Cost: —";


    document.getElementById(
        "longestText"
    ).textContent = "Cost: —";


    document.getElementById(
        "smartChoice"
    ).textContent =
        "Run comparison to see the result";


    document.getElementById(
        "aiInsight"
    ).textContent =
        "Select a route and compare algorithms.";


    document.getElementById(
        "routeLayerDijkstra"
    ).innerHTML = "";


    document.getElementById(
        "routeLayerAstar"
    ).innerHTML = "";


    explorationLayer.innerHTML = "";


    drawNodes();

    markStartGoal();

    applyModeRoadStyle();
}


// ============================================================
// START / GOAL
// ============================================================

function markStartGoal() {

    const start =
        startSelect.value;

    const goal =
        goalSelect.value;


    const startGroup =
        document.getElementById(
            `node-${start}`
        );


    const goalGroup =
        document.getElementById(
            `node-${goal}`
        );


    if (startGroup) {

        startGroup
            .querySelector("circle")
            .classList.add(
                "start-node"
            );

    }


    if (goalGroup) {

        goalGroup
            .querySelector("circle")
            .classList.add(
                "goal-node"
            );

    }
}


// ============================================================
// CHECK WHEELCHAIR ROUTE
// ============================================================

function wheelchairRouteIsValid(path) {

    if (mode !== "wheelchair") {
        return true;
    }


    if (!path || path.length < 2) {
        return true;
    }


    for (
        let i = 0;
        i < path.length - 1;
        i++
    ) {

        const a = path[i];

        const b = path[i + 1];


        if (isStairEdge(a, b)) {

            return false;

        }

    }


    return true;
}


// ============================================================
// SEARCH
// ============================================================

async function startSearch() {

    if (searching) {
        return;
    }


    const start =
        startSelect.value;

    const goal =
        goalSelect.value;


    resetDemo();


    searching = true;


    try {

        const response =
            await fetch(
                `/results?start=${encodeURIComponent(start)}&goal=${encodeURIComponent(goal)}&mode=${encodeURIComponent(mode)}`
            );


        if (!response.ok) {

            throw new Error(
                "Backend response failed"
            );

        }


        const data =
            await response.json();


        currentData = data;


        // =================================================
        // HARD WHEELCHAIR VALIDATION
        // =================================================

        if (
            mode === "wheelchair" &&
            (
                !wheelchairRouteIsValid(
                    data.dijkstra.path
                )
                ||
                !wheelchairRouteIsValid(
                    data.astar.path
                )
            )
        ) {

            throw new Error(
                "Wheelchair route contains a stair edge."
            );

        }


        updateInitialResult(
            data
        );


        await Promise.all([

            animateAlgorithm(
                "dijkstra",
                data.dijkstra
            ),

            animateAlgorithm(
                "astar",
                data.astar
            )

        ]);


        showPath(
            "dijkstra",
            data.dijkstra.path
        );


        showPath(
            "astar",
            data.astar.path
        );


        updateAnalysis(
            data
        );


        searching = false;

    }
    catch (error) {

        console.error(error);


        document.getElementById(
            "aiInsight"
        ).textContent =
            error.message;


        searching = false;

    }
}


// ============================================================
// RESULT HEADER
// ============================================================

function updateInitialResult(data) {

    const d =
        data.dijkstra;

    const a =
        data.astar;


    document.getElementById(
        "dijkstraDistance"
    ).textContent =
        d.path && d.path.length
            ? `${d.path.length} nodes`
            : "No route";


    document.getElementById(
        "astarDistance"
    ).textContent =
        a.path && a.path.length
            ? `${a.path.length} nodes`
            : "No route";


    document.getElementById(
        "dijkstraCost"
    ).textContent =
        d.cost !== null
            ? d.cost
            : "—";


    document.getElementById(
        "astarCost"
    ).textContent =
        a.cost !== null
            ? a.cost
            : "—";


    document.getElementById(
        "dijkstraRoute"
    ).textContent =
        d.path && d.path.length
            ? d.path.join(" → ")
            : "No accessible route";


    document.getElementById(
        "astarRoute"
    ).textContent =
        a.path && a.path.length
            ? a.path.join(" → ")
            : "No accessible route";
}


// ============================================================
// ANIMATION
// ============================================================

async function animateAlgorithm(
    algorithm,
    result
) {

    const counterId =
        algorithm === "dijkstra"
            ? "dijkstraCounter"
            : "astarCounter";


    const explored =
        result.explored || [];


    for (
        let i = 0;
        i < explored.length;
        i++
    ) {

        const node =
            explored[i];


        const group =
            document.getElementById(
                `node-${node}`
            );


        if (group) {

            group
                .querySelector("circle")
                .classList.add(
                    "search-node"
                );

        }


        addExplorationDot(
            node
        );


        document.getElementById(
            counterId
        ).textContent =
            i + 1;


        await wait(130);

    }
}


// ============================================================
// SEARCH DOT
// ============================================================

function addExplorationDot(node) {

    const p =
        NODES[node];


    if (!p) {
        return;
    }


    const circle =
        document.createElementNS(
            "http://www.w3.org/2000/svg",
            "circle"
        );


    circle.setAttribute(
        "cx",
        p.x
    );


    circle.setAttribute(
        "cy",
        p.y
    );


    circle.setAttribute(
        "r",
        5
    );


    circle.classList.add(
        "explored-dot"
    );


    explorationLayer.appendChild(
        circle
    );
}


// ============================================================
// DRAW COMPLETE ROUTE
// ============================================================

function showPath(
    algorithm,
    path
) {

    if (
        !path ||
        path.length < 2
    ) {
        return;
    }


    // FINAL SAFETY CHECK
    if (
        mode === "wheelchair" &&
        !wheelchairRouteIsValid(path)
    ) {

        return;

    }


    const layer =
        document.getElementById(
            algorithm === "dijkstra"
                ? "routeLayerDijkstra"
                : "routeLayerAstar"
        );


    layer.innerHTML = "";


    const polyline =
        document.createElementNS(
            "http://www.w3.org/2000/svg",
            "polyline"
        );


    const points =
        path
            .filter(
                node =>
                    NODES[node]
            )
            .map(
                node =>
                    `${NODES[node].x},${NODES[node].y}`
            )
            .join(" ");


    polyline.setAttribute(
        "points",
        points
    );


    polyline.classList.add(
        algorithm === "dijkstra"
            ? "route-dijkstra"
            : "route-astar"
    );


    layer.appendChild(
        polyline
    );


    // Highlight route nodes

    path.forEach(
        node => {

            const group =
                document.getElementById(
                    `node-${node}`
                );


            if (!group) {
                return;
            }


            const circle =
                group.querySelector(
                    "circle"
                );


            if (
                node === startSelect.value
            ) {

                circle.classList.add(
                    "start-node"
                );

            }

            else if (
                node === goalSelect.value
            ) {

                circle.classList.add(
                    "goal-node"
                );

            }

            else if (
                algorithm === "dijkstra"
            ) {

                circle.classList.add(
                    "path-node-dijkstra"
                );

            }

            else {

                circle.classList.add(
                    "path-node-astar"
                );

            }

        }
    );
}


// ============================================================
// ANALYSIS
// ============================================================

function updateAnalysis(data) {

    const shortest =
        data.shortest || {};

    const safest =
        data.safest || {};

    const longest =
        data.longest || {};


    document.getElementById(
        "shortestText"
    ).textContent =
        shortest.path &&
        shortest.path.length
            ? `Cost: ${shortest.cost} | ${shortest.path.join(" → ")}`
            : "No route";


    document.getElementById(
        "safestText"
    ).textContent =
        safest.path &&
        safest.path.length
            ? `Cost: ${safest.cost} | ${safest.path.join(" → ")}`
            : "No safe route";


    document.getElementById(
        "longestText"
    ).textContent =
        longest.path &&
        longest.path.length
            ? `Cost: ${longest.cost} | ${longest.path.length} nodes`
            : "No route";


    chooseSmartRoute(
        data
    );
}


// ============================================================
// SMART CHOICE
// ============================================================

function chooseSmartRoute(data) {

    let message = "";

    let insight = "";


    if (mode === "wheelchair") {

        message =
            "♿ Accessible route selected.";

        insight =
            "Stair segments are treated as blocked edges. The algorithm searches for an alternative accessible route.";

    }


    else if (mode === "women") {

        message =
            "👩 Safety-focused route selected.";

        insight =
            "CCTV-covered, well-lit and active roads receive preference.";

    }


    else {

        message =
            "⚡ Route comparison completed.";

        insight =
            "Dijkstra and A* explore the same road network using different search strategies.";

    }


    document.getElementById(
        "smartChoice"
    ).textContent =
        message;


    document.getElementById(
        "aiInsight"
    ).textContent =
        insight;
}


// ============================================================
// UTILITY
// ============================================================

function wait(ms) {

    return new Promise(
        resolve =>
            setTimeout(
                resolve,
                ms
            )
    );
}