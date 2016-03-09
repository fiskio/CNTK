# This file is auto-generated by _fetch_ops.py.

from cntk.graph import ComputationNode

class LearnableParameter(ComputationNode):
    def __init__(self, rows, cols, learningRateMultiplier=1.0, init='uniform', initValueScale=1, value=0, initFromFilePath='', initOnCPUOnly=True, randomSeed=-1, name='LearnableParameter'):
        super(LearnableParameter, self).__init__(params=['rows', 'cols', 'learningRateMultiplier', 'init', 'initValueScale', 'value', 'initFromFilePath', 'initOnCPUOnly', 'randomSeed'], name=name)
        self.rows = rows
        self.cols = cols
        self.learningRateMultiplier = learningRateMultiplier
        self.init = init
        self.initValueScale = initValueScale
        self.value = value
        self.initFromFilePath = initFromFilePath
        self.initOnCPUOnly = initOnCPUOnly
        self.randomSeed = randomSeed

class ParameterTensor(ComputationNode):
    def __init__(self, dims, learningRateMultiplier=1.0, init='uniform', initValueScale=1, value=0, initFromFilePath='', initOnCPUOnly=True, randomSeed=-1, name='ParameterTensor'):
        super(ParameterTensor, self).__init__(params=['dims', 'learningRateMultiplier', 'init', 'initValueScale', 'value', 'initFromFilePath', 'initOnCPUOnly', 'randomSeed'], name=name)
        self.dims = dims
        self.learningRateMultiplier = learningRateMultiplier
        self.init = init
        self.initValueScale = initValueScale
        self.value = value
        self.initFromFilePath = initFromFilePath
        self.initOnCPUOnly = initOnCPUOnly
        self.randomSeed = randomSeed

class Input(ComputationNode):
    def __init__(self, dims, tag='feature', name='Input'):
        super(Input, self).__init__(params=['dims', 'tag'], name=name)
        self.dims = dims
        self.tag = tag

class SparseInput(ComputationNode):
    def __init__(self, dims, tag='feature', name='SparseInput'):
        super(SparseInput, self).__init__(params=['dims', 'tag'], name=name)
        self.dims = dims
        self.tag = tag

class ImageInput(ComputationNode):
    def __init__(self, imageWidth, imageHeight, imageChannels, imageLayout='CHW', tag='feature', name='ImageInput'):
        super(ImageInput, self).__init__(params=['imageWidth', 'imageHeight', 'imageChannels', 'imageLayout', 'tag'], name=name)
        self.imageWidth = imageWidth
        self.imageHeight = imageHeight
        self.imageChannels = imageChannels
        self.imageLayout = imageLayout
        self.tag = tag

class SparseImageInput(ComputationNode):
    def __init__(self, imageWidth, imageHeight, imageChannels, imageLayout='CHW', tag='feature', name='SparseImageInput'):
        super(SparseImageInput, self).__init__(params=['imageWidth', 'imageHeight', 'imageChannels', 'imageLayout', 'tag'], name=name)
        self.imageWidth = imageWidth
        self.imageHeight = imageHeight
        self.imageChannels = imageChannels
        self.imageLayout = imageLayout
        self.tag = tag

class PastValue(ComputationNode):
    def __init__(self, dims, input, timeStep=1, defaultHiddenActivation=0.1, name='PastValue'):
        super(PastValue, self).__init__(params=['dims', 'input', 'timeStep', 'defaultHiddenActivation'], name=name)
        self.dims = dims
        self.input = input
        self.timeStep = timeStep
        self.defaultHiddenActivation = defaultHiddenActivation

class FutureValue(ComputationNode):
    def __init__(self, dims, input, timeStep=1, defaultHiddenActivation=0.1, name='FutureValue'):
        super(FutureValue, self).__init__(params=['dims', 'input', 'timeStep', 'defaultHiddenActivation'], name=name)
        self.dims = dims
        self.input = input
        self.timeStep = timeStep
        self.defaultHiddenActivation = defaultHiddenActivation

class Shift(ComputationNode):
    def __init__(self, input, fromOffset, boundaryValue, boundaryMode=-1, dim=-1, name='Shift'):
        super(Shift, self).__init__(params=['input', 'fromOffset', 'boundaryValue', 'boundaryMode', 'dim'], name=name)
        self.input = input
        self.fromOffset = fromOffset
        self.boundaryValue = boundaryValue
        self.boundaryMode = boundaryMode
        self.dim = dim

class RowSlice(ComputationNode):
    def __init__(self, startIndex, numRows, input, name='RowSlice'):
        super(RowSlice, self).__init__(params=['startIndex', 'numRows', 'input'], name=name)
        self.startIndex = startIndex
        self.numRows = numRows
        self.input = input

class RowRepeat(ComputationNode):
    def __init__(self, input, numRepeats, name='RowRepeat'):
        super(RowRepeat, self).__init__(params=['input', 'numRepeats'], name=name)
        self.input = input
        self.numRepeats = numRepeats

class RowStack(ComputationNode):
    def __init__(self, inputs, name='RowStack'):
        super(RowStack, self).__init__(params=['inputs'], name=name)
        self.inputs = inputs

class Reshape(ComputationNode):
    def __init__(self, input, numRows, imageWidth=0, imageHeight=0, imageChannels=0, name='Reshape'):
        super(Reshape, self).__init__(params=['input', 'numRows', 'imageWidth', 'imageHeight', 'imageChannels'], name=name)
        self.input = input
        self.numRows = numRows
        self.imageWidth = imageWidth
        self.imageHeight = imageHeight
        self.imageChannels = imageChannels

class NewReshape(ComputationNode):
    def __init__(self, input, dims, beginDim=0, endDim=0, name='NewReshape'):
        super(NewReshape, self).__init__(params=['input', 'dims', 'beginDim', 'endDim'], name=name)
        self.input = input
        self.dims = dims
        self.beginDim = beginDim
        self.endDim = endDim

class TransposeDimensions(ComputationNode):
    def __init__(self, input, dim1, dim2, name='TransposeDimensions'):
        super(TransposeDimensions, self).__init__(params=['input', 'dim1', 'dim2'], name=name)
        self.input = input
        self.dim1 = dim1
        self.dim2 = dim2

class Times(ComputationNode):
    def __init__(self, A, B, outputRank=1, name='Times'):
        super(Times, self).__init__(params=['A', 'B', 'outputRank'], name=name)
        self.A = A
        self.B = B
        self.outputRank = outputRank

class Logistic(ComputationNode):
    def __init__(self, label, probability, name='Logistic'):
        super(Logistic, self).__init__(params=['label', 'probability'], name=name)
        self.label = label
        self.probability = probability

class WeightedLogistic(ComputationNode):
    def __init__(self, label, probability, instanceWeight, name='WeightedLogistic'):
        super(WeightedLogistic, self).__init__(params=['label', 'probability', 'instanceWeight'], name=name)
        self.label = label
        self.probability = probability
        self.instanceWeight = instanceWeight

class ReconcileMBLayout(ComputationNode):
    def __init__(self, dataInput, layoutInput, name='ReconcileMBLayout'):
        super(ReconcileMBLayout, self).__init__(params=['dataInput', 'layoutInput'], name=name)
        self.dataInput = dataInput
        self.layoutInput = layoutInput

class Convolution(ComputationNode):
    def __init__(self, weightNode, inputValueNode, kernelWidth, kernelHeight, outputChannels, horizontalSubsample, verticalSubsample, zeroPadding=False, maxTempMemSizeInSamples=0, imageLayout='CHW', name='Convolution'):
        super(Convolution, self).__init__(params=['weightNode', 'inputValueNode', 'kernelWidth', 'kernelHeight', 'outputChannels', 'horizontalSubsample', 'verticalSubsample', 'zeroPadding', 'maxTempMemSizeInSamples', 'imageLayout'], name=name)
        self.weightNode = weightNode
        self.inputValueNode = inputValueNode
        self.kernelWidth = kernelWidth
        self.kernelHeight = kernelHeight
        self.outputChannels = outputChannels
        self.horizontalSubsample = horizontalSubsample
        self.verticalSubsample = verticalSubsample
        self.zeroPadding = zeroPadding
        self.maxTempMemSizeInSamples = maxTempMemSizeInSamples
        self.imageLayout = imageLayout

class MaxPooling(ComputationNode):
    def __init__(self, input, windowWidth, windowHeight, horizontalSubsample, verticalSubsample, imageLayout='CHW', name='MaxPooling'):
        super(MaxPooling, self).__init__(params=['input', 'windowWidth', 'windowHeight', 'horizontalSubsample', 'verticalSubsample', 'imageLayout'], name=name)
        self.input = input
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.horizontalSubsample = horizontalSubsample
        self.verticalSubsample = verticalSubsample
        self.imageLayout = imageLayout

class AveragePooling(ComputationNode):
    def __init__(self, input, windowWidth, windowHeight, horizontalSubsample, verticalSubsample, imageLayout='CHW', name='AveragePooling'):
        super(AveragePooling, self).__init__(params=['input', 'windowWidth', 'windowHeight', 'horizontalSubsample', 'verticalSubsample', 'imageLayout'], name=name)
        self.input = input
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.horizontalSubsample = horizontalSubsample
        self.verticalSubsample = verticalSubsample
        self.imageLayout = imageLayout

class BatchNormalization(ComputationNode):
    def __init__(self, input, scale, bias, runMean, runInvStdDev, eval, spatial, normalizationTimeConstant=0, epsilon=1e-05, useCntkEngine=True, imageLayout='CHW', name='BatchNormalization'):
        super(BatchNormalization, self).__init__(params=['input', 'scale', 'bias', 'runMean', 'runInvStdDev', 'eval', 'spatial', 'normalizationTimeConstant', 'epsilon', 'useCntkEngine', 'imageLayout'], name=name)
        self.input = input
        self.scale = scale
        self.bias = bias
        self.runMean = runMean
        self.runInvStdDev = runInvStdDev
        self.eval = eval
        self.spatial = spatial
        self.normalizationTimeConstant = normalizationTimeConstant
        self.epsilon = epsilon
        self.useCntkEngine = useCntkEngine
        self.imageLayout = imageLayout

class ClassBasedCrossEntropyWithSoftmax(ComputationNode):
    def __init__(self, labelClassDescriptorVectorSequence, mainInputInfo, mainWeight, classLogProbsBeforeSoftmax, name='ClassBasedCrossEntropyWithSoftmax'):
        super(ClassBasedCrossEntropyWithSoftmax, self).__init__(params=['labelClassDescriptorVectorSequence', 'mainInputInfo', 'mainWeight', 'classLogProbsBeforeSoftmax'], name=name)
        self.labelClassDescriptorVectorSequence = labelClassDescriptorVectorSequence
        self.mainInputInfo = mainInputInfo
        self.mainWeight = mainWeight
        self.classLogProbsBeforeSoftmax = classLogProbsBeforeSoftmax

class ColumnElementTimes(ComputationNode):
    def __init__(self, aVectorSequence, anotherVectorSequence, name='ColumnElementTimes'):
        super(ColumnElementTimes, self).__init__(params=['aVectorSequence', 'anotherVectorSequence'], name=name)
        self.aVectorSequence = aVectorSequence
        self.anotherVectorSequence = anotherVectorSequence

class CosDistance(ComputationNode):
    def __init__(self, aVectorSequence, anotherVectorSequence, name='CosDistance'):
        super(CosDistance, self).__init__(params=['aVectorSequence', 'anotherVectorSequence'], name=name)
        self.aVectorSequence = aVectorSequence
        self.anotherVectorSequence = anotherVectorSequence

class CosDistanceWithNegativeSamples(ComputationNode):
    def __init__(self, aVectorSequence, anotherVectorSequence, numShifts, numNegSamples, name='CosDistanceWithNegativeSamples'):
        super(CosDistanceWithNegativeSamples, self).__init__(params=['aVectorSequence', 'anotherVectorSequence', 'numShifts', 'numNegSamples'], name=name)
        self.aVectorSequence = aVectorSequence
        self.anotherVectorSequence = anotherVectorSequence
        self.numShifts = numShifts
        self.numNegSamples = numNegSamples

class Cosine(ComputationNode):
    def __init__(self, x, name='Cosine'):
        super(Cosine, self).__init__(params=['x'], name=name)
        self.x = x

class CrossEntropy(ComputationNode):
    def __init__(self, refProbVectorSequence, outProbVectorSequence, name='CrossEntropy'):
        super(CrossEntropy, self).__init__(params=['refProbVectorSequence', 'outProbVectorSequence'], name=name)
        self.refProbVectorSequence = refProbVectorSequence
        self.outProbVectorSequence = outProbVectorSequence

class CrossEntropyWithSoftmax(ComputationNode):
    def __init__(self, labelVectorSequence, outProbVectorSequence, name='CrossEntropyWithSoftmax'):
        super(CrossEntropyWithSoftmax, self).__init__(params=['labelVectorSequence', 'outProbVectorSequence'], name=name)
        self.labelVectorSequence = labelVectorSequence
        self.outProbVectorSequence = outProbVectorSequence

class DiagTimes(ComputationNode):
    def __init__(self, diagonalMatrixAsColumnVector, matrix, name='DiagTimes'):
        super(DiagTimes, self).__init__(params=['diagonalMatrixAsColumnVector', 'matrix'], name=name)
        self.diagonalMatrixAsColumnVector = diagonalMatrixAsColumnVector
        self.matrix = matrix

class Dropout(ComputationNode):
    def __init__(self, activationVectorSequence, name='Dropout'):
        super(Dropout, self).__init__(params=['activationVectorSequence'], name=name)
        self.activationVectorSequence = activationVectorSequence

class ElementTimes(ComputationNode):
    def __init__(self, aMatrix, anotherMatrix, name='ElementTimes'):
        super(ElementTimes, self).__init__(params=['aMatrix', 'anotherMatrix'], name=name)
        self.aMatrix = aMatrix
        self.anotherMatrix = anotherMatrix

class ErrorPrediction(ComputationNode):
    def __init__(self, labelVectorSequence, outVectorSequence, name='ErrorPrediction'):
        super(ErrorPrediction, self).__init__(params=['labelVectorSequence', 'outVectorSequence'], name=name)
        self.labelVectorSequence = labelVectorSequence
        self.outVectorSequence = outVectorSequence

class Exp(ComputationNode):
    def __init__(self, x, name='Exp'):
        super(Exp, self).__init__(params=['x'], name=name)
        self.x = x

class GMMLogLikelihood(ComputationNode):
    def __init__(self, unnormalizedPriorVector, meansAsRows, logStdDevAsRows, dataVectorSequence, name='GMMLogLikelihood'):
        super(GMMLogLikelihood, self).__init__(params=['unnormalizedPriorVector', 'meansAsRows', 'logStdDevAsRows', 'dataVectorSequence'], name=name)
        self.unnormalizedPriorVector = unnormalizedPriorVector
        self.meansAsRows = meansAsRows
        self.logStdDevAsRows = logStdDevAsRows
        self.dataVectorSequence = dataVectorSequence

class InvStdDev(ComputationNode):
    def __init__(self, dataVectorSequence, name='InvStdDev'):
        super(InvStdDev, self).__init__(params=['dataVectorSequence'], name=name)
        self.dataVectorSequence = dataVectorSequence

class KhatriRaoProduct(ComputationNode):
    def __init__(self, leftMatrix, rightMatrix, name='KhatriRaoProduct'):
        super(KhatriRaoProduct, self).__init__(params=['leftMatrix', 'rightMatrix'], name=name)
        self.leftMatrix = leftMatrix
        self.rightMatrix = rightMatrix

class Log(ComputationNode):
    def __init__(self, x, name='Log'):
        super(Log, self).__init__(params=['x'], name=name)
        self.x = x

class LogSoftmax(ComputationNode):
    def __init__(self, z, name='LogSoftmax'):
        super(LogSoftmax, self).__init__(params=['z'], name=name)
        self.z = z

class MatrixL1Reg(ComputationNode):
    def __init__(self, matrix, name='MatrixL1Reg'):
        super(MatrixL1Reg, self).__init__(params=['matrix'], name=name)
        self.matrix = matrix

class MatrixL2Reg(ComputationNode):
    def __init__(self, matrix, name='MatrixL2Reg'):
        super(MatrixL2Reg, self).__init__(params=['matrix'], name=name)
        self.matrix = matrix

class Mean(ComputationNode):
    def __init__(self, dataVectorSequence, name='Mean'):
        super(Mean, self).__init__(params=['dataVectorSequence'], name=name)
        self.dataVectorSequence = dataVectorSequence

class Minus(ComputationNode):
    def __init__(self, leftMatrix, rightMatrix, name='Minus'):
        super(Minus, self).__init__(params=['leftMatrix', 'rightMatrix'], name=name)
        self.leftMatrix = leftMatrix
        self.rightMatrix = rightMatrix

class Negate(ComputationNode):
    def __init__(self, input, name='Negate'):
        super(Negate, self).__init__(params=['input'], name=name)
        self.input = input

class PerDimMeanVarDeNormalization(ComputationNode):
    def __init__(self, dataVectorSequence, meanVector, invStdDevVector, name='PerDimMeanVarDeNormalization'):
        super(PerDimMeanVarDeNormalization, self).__init__(params=['dataVectorSequence', 'meanVector', 'invStdDevVector'], name=name)
        self.dataVectorSequence = dataVectorSequence
        self.meanVector = meanVector
        self.invStdDevVector = invStdDevVector

class PerDimMeanVarNormalization(ComputationNode):
    def __init__(self, dataVectorSequence, meanVector, invStdDevVector, name='PerDimMeanVarNormalization'):
        super(PerDimMeanVarNormalization, self).__init__(params=['dataVectorSequence', 'meanVector', 'invStdDevVector'], name=name)
        self.dataVectorSequence = dataVectorSequence
        self.meanVector = meanVector
        self.invStdDevVector = invStdDevVector

class Plus(ComputationNode):
    def __init__(self, leftMatrix, rightMatrix, name='Plus'):
        super(Plus, self).__init__(params=['leftMatrix', 'rightMatrix'], name=name)
        self.leftMatrix = leftMatrix
        self.rightMatrix = rightMatrix

class RectifiedLinear(ComputationNode):
    def __init__(self, z, name='RectifiedLinear'):
        super(RectifiedLinear, self).__init__(params=['z'], name=name)
        self.z = z

class Scale(ComputationNode):
    def __init__(self, scalarScalingFactor, matrix, name='Scale'):
        super(Scale, self).__init__(params=['scalarScalingFactor', 'matrix'], name=name)
        self.scalarScalingFactor = scalarScalingFactor
        self.matrix = matrix

class Sigmoid(ComputationNode):
    def __init__(self, z, name='Sigmoid'):
        super(Sigmoid, self).__init__(params=['z'], name=name)
        self.z = z

class Softmax(ComputationNode):
    def __init__(self, z, name='Softmax'):
        super(Softmax, self).__init__(params=['z'], name=name)
        self.z = z

class Hardmax(ComputationNode):
    def __init__(self, z, name='Hardmax'):
        super(Hardmax, self).__init__(params=['z'], name=name)
        self.z = z

class SquareError(ComputationNode):
    def __init__(self, aMatrix, anotherMatrix, name='SquareError'):
        super(SquareError, self).__init__(params=['aMatrix', 'anotherMatrix'], name=name)
        self.aMatrix = aMatrix
        self.anotherMatrix = anotherMatrix

class SumColumnElements(ComputationNode):
    def __init__(self, z, name='SumColumnElements'):
        super(SumColumnElements, self).__init__(params=['z'], name=name)
        self.z = z

class SumElements(ComputationNode):
    def __init__(self, matrix, name='SumElements'):
        super(SumElements, self).__init__(params=['matrix'], name=name)
        self.matrix = matrix

class Tanh(ComputationNode):
    def __init__(self, z, name='Tanh'):
        super(Tanh, self).__init__(params=['z'], name=name)
        self.z = z

class TimeReverse(ComputationNode):
    def __init__(self, vectorSequence, name='TimeReverse'):
        super(TimeReverse, self).__init__(params=['vectorSequence'], name=name)
        self.vectorSequence = vectorSequence

class TransposeTimes(ComputationNode):
    def __init__(self, leftMatrix, rightMatrix, name='TransposeTimes'):
        super(TransposeTimes, self).__init__(params=['leftMatrix', 'rightMatrix'], name=name)
        self.leftMatrix = leftMatrix
        self.rightMatrix = rightMatrix

Parameter = LearnableParameter
ColumnwiseCrossProduct = KhatriRaoProduct
ClassificationError = ErrorPrediction
Delay = PastValue
class Constant(Parameter):
    def __init__(self, value, rows=1, cols=1, name='Constant'):
        super(Constant, self).__init__(rows, cols, learningRateMultiplier=0, init='fixedValue', value=value, name=name)
        self.params=['value', 'rows', 'cols']

class ReshapeDimension(NewReshape):
    def __init__(self, x, dim, tensorShape, name='ReshapeDimension'):
        super(ReshapeDimension, self).__init__(x, tensorShape, beginDim=dim, endDim=dim + 1, name=name)
        self.params=['x', 'dim', 'tensorShape']

class FlattenDimensions(NewReshape):
    def __init__(self, x, dim, num, name='FlattenDimensions'):
        super(FlattenDimensions, self).__init__(x, 0, beginDim=dim, endDim=dim + num, name=name)
        self.params=['x', 'dim', 'num']

class SplitDimension(ReshapeDimension):
    def __init__(self, x, dim, N, name='SplitDimension'):
        super(SplitDimension, self).__init__(x, dim, N, name=name)
        self.params=['x', 'dim', 'N']

class Transpose(TransposeDimensions):
    def __init__(self, x, name='Transpose'):
        super(Transpose, self).__init__(x, 1, 2, name=name)
        self.params=['x']
