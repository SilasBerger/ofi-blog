
const DOM_ELEMENT_IDS = {
    component: (codeId) => `py_${codeId}`,
    graphicsResult: (codeId) => `${codeId}_graphics`,
    outputDiv: (codeId) => `${codeId}_brython_result`,
    aceEditor: (codeId) => `${codeId}_editor`,
    turtleSvgContainer: (codeId) => `${codeId}_svg`,
    canvasContainer: (codeId) => `${codeId}_canvas`,
    scriptSource: (codeId) => `${codeId}_src`
}

const BRYTHON_NOTIFICATION_EVENT = 'bry_notify'
const CLOSE_TURTLE_MODAL_EVENT = 'close_turtle_modal'
const TURTLE_IMPORTS_TESTER = /(^from turtle import)|(^import turtle)/m
const TURTLE3D_IMPORTS_TESTER = /(^from turtle3d import)|(^import turtle3d)/m
const GRID_IMPORTS_TESTER = /(^from grid import)|(^import grid)/m
const GRAPHICS_OUTPUT_TESTER = /^(SETUP_)?GRAPHICS_OUTPUT\s*=\s*(True|1)/m
const CANVAS_OUTPUT_TESTER = /^(SETUP_)?CANVAS_OUTPUT\s*=\s*(True|1)/m


export {
    DOM_ELEMENT_IDS,
    BRYTHON_NOTIFICATION_EVENT,
    CLOSE_TURTLE_MODAL_EVENT,
    TURTLE_IMPORTS_TESTER,
    GRAPHICS_OUTPUT_TESTER,
    CANVAS_OUTPUT_TESTER,
    GRID_IMPORTS_TESTER,
    TURTLE3D_IMPORTS_TESTER
}