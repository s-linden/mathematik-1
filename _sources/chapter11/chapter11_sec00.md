# Differentialrechnung (Teil 2)


JSXGraph:

<script type="text/javascript" charset="UTF-8"
 src="https://cdn.jsdelivr.net/npm/jsxgraph/distrib/jsxgraphcore.js">
 </script>


<div id="jxgbox" class="jxgbox" style="width:500px; height:200px;"></div>
<script type="text/javascript">
JXG.Options.label.autoPosition = true;
JXG.Options.text.fontSize = 16;
JXG.Options.line.strokeWidth = 0.8;
var board = JXG.JSXGraph.initBoard('jxgbox', { boundingbox: [-5, 5, 5, -5], axis: true, showClearTraces: true});
var h = board.create('hyperbola', [[-Math.sqrt(2),0], [Math.sqrt(2),0], [2, Math.sqrt(3)]]);
var l1 = board.create('line', [0, 1, 1], {dash: 1});
var l2 = board.create('line', [0, -1, 1], {dash: 1});
</script>