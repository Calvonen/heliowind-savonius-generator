plate_thickness = 6;
shaft_hole = 12;

$fn = 180;

// [10:400]
height = 460;

// [50:200]
radius = 110;

// [50:200]
blade_width = 110;

// [1:10]
blade_thickness = 1.5;

// [0:360]
twist_angle = 180;

linear_extrude(
    height = height,
    twist = twist_angle,
    slices = 200,
    convexity = 10
)
translate([radius,0,0])
offset(r=8)
square(
    [blade_width, blade_thickness],
    center=true
);
for(angle = [0,120,240])

rotate([0,0,angle])

linear_extrude(
    height = height,
    twist = twist_angle,
    slices = 200,
    convexity = 10
)

translate([radius,0,0])

offset(r=8)

square(
    [blade_width, blade_thickness],
    center=true
);
linear_extrude(
    height = height,
    twist = twist_angle,
    slices = 200,
    convexity = 10
)
translate([radius,0,0])
offset(r=8)
square(
    [blade_width, blade_thickness],
    center=true
);
difference() {
    cylinder(
        h = plate_thickness,
        r = radius + 80
    );

    cylinder(
        h = plate_thickness + 1,
        r = shaft_hole / 2
    );
}

translate([0,0,height])
difference() {
    cylinder(
        h = plate_thickness,
        r = radius + 80
    );

    cylinder(
        h = plate_thickness + 1,
        r = shaft_hole / 2
    );
}
cylinder(h=height, r=8);