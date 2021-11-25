using System;
using System.IO;
using System.Text;
using MathNet.Numerics;
using MathNet.Numerics.LinearAlgebra;
using MathNet.Numerics.LinearAlgebra.Double;

class Program
{
    static void Main(string[] args)
    {
        // Evaluate a special function
        Console.WriteLine(SpecialFunctions.Erf(0.5));

        // Solve a random linear equation system with 500 unknowns
        var m = Matrix<double>.Build.Random(500, 500);
        var v = Vector<double>.Build.Random(500);
        var y = m.Solve(v);
        Console.WriteLine(y);

        // A to find an orthonormal basis of the kernel or null-space of that matrix, such that
        // Ax = 0  for all x  in that subspace.
        Matrix<double> A = DenseMatrix.OfArray(new double[,] {
                {1,1,1,1},
                {1,2,3,4},
                {4,3,2,1}});
        Vector<double>[] nullspace = A.Kernel();

        // verify: the following should be approximately (0,0,0)
        (A * (2*nullspace[0] - 3*nullspace[1]))

    }
}

// Geolib
string wkt = "POINT (10 20)";
var point = Geometry.FromWkt(wkt);
var pointWkt = point.ToWkt();

string path = @"";
string geoJson = File.ReadAllText(path);
string geoJson = "{\"type\": \"LineString\", \"coordinates\": [[30, 10], [10, 30], [40, 40]] }"
var lineString = Geometry.FromGeoJson(geoJson);
var lineStringGeoJson = lineString.ToGeoJson();

// GeoJSON
// Serialization
Position position = new Position(51.899523, -2.124156);
Point point = new Point(position);
string json = JsonConvert.SerializeObject(point);

// Deserialization
string path = @"";
string geoJson = File.ReadAllText(path);
string geoJson = "{\"coordinates\":[-2.124156,51.899523],\"type\":\"Point\"}";
Point point = JsonConvert.DeserializeObject<Point>(geoJson);
