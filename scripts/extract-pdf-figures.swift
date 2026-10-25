#!/usr/bin/env swift
import Foundation
import PDFKit
import AppKit

struct CropSpec {
    let pageNumber: Int // 1-based
    let x: CGFloat      // normalized 0..1 from left
    let y: CGFloat      // normalized 0..1 from bottom (PDF coordinate space)
    let w: CGFloat      // normalized width 0..1
    let h: CGFloat      // normalized height 0..1
    let outputPath: String
}

let args = CommandLine.arguments
guard args.count >= 2 else {
    print("Usage: extract-pdf-figures.swift <pdf-path> [output-dir]")
    exit(1)
}

let pdfPath = args[1]
let outDir = args.count >= 3 ? args[2] : "/Users/jsoftware/edu/graduate-study/docs/computer-networks/images"

guard let doc = PDFDocument(url: URL(fileURLWithPath: pdfPath)) else {
    fputs("Failed to open PDF: \(pdfPath)\n", stderr)
    exit(1)
}

let specs: [CropSpec] = [
    CropSpec(pageNumber: 10, x: 0.05, y: 0.10, w: 0.94, h: 0.34, outputPath: "\(outDir)/ch05-routing-table-example.png"),
    CropSpec(pageNumber: 11, x: 0.05, y: 0.11, w: 0.93, h: 0.86, outputPath: "\(outDir)/ch05-route-print-ipv4.png"),
    CropSpec(pageNumber: 13, x: 0.05, y: 0.43, w: 0.85, h: 0.39, outputPath: "\(outDir)/ch05-arp-table.png"),
    CropSpec(pageNumber: 16, x: 0.60, y: 0.48, w: 0.35, h: 0.40, outputPath: "\(outDir)/ch05-flow-vs-congestion-control.png"),
    CropSpec(pageNumber: 19, x: 0.06, y: 0.08, w: 0.92, h: 0.54, outputPath: "\(outDir)/ch05-token-vs-leaky-bucket.png"),
    CropSpec(pageNumber: 22, x: 0.10, y: 0.16, w: 0.62, h: 0.28, outputPath: "\(outDir)/ch05-ecn-notification.png")
]

let scale: CGFloat = 2.0
let fm = FileManager.default

for spec in specs {
    if fm.fileExists(atPath: spec.outputPath) {
        print("[SKIP] Already exists (never overwrite): \(spec.outputPath)")
        continue
    }
    guard let page = doc.page(at: spec.pageNumber - 1) else {
        fputs("Invalid page \(spec.pageNumber)\n", stderr)
        continue
    }
    let bounds = page.bounds(for: .mediaBox)
    let cropRect = CGRect(
        x: bounds.origin.x + bounds.width * spec.x,
        y: bounds.origin.y + bounds.height * spec.y,
        width: bounds.width * spec.w,
        height: bounds.height * spec.h
    )
    let pixelW = Int(cropRect.width * scale)
    let pixelH = Int(cropRect.height * scale)

    guard let bitmap = NSBitmapImageRep(
        bitmapDataPlanes: nil,
        pixelsWide: pixelW,
        pixelsHigh: pixelH,
        bitsPerSample: 8,
        samplesPerPixel: 4,
        hasAlpha: true,
        isPlanar: false,
        colorSpaceName: .deviceRGB,
        bytesPerRow: 0,
        bitsPerPixel: 0
    ) else { continue }

    NSGraphicsContext.saveGraphicsState()
    if let ctx = NSGraphicsContext(bitmapImageRep: bitmap) {
        NSGraphicsContext.current = ctx
        let cg = ctx.cgContext
        cg.setFillColor(NSColor.white.cgColor)
        cg.fill(CGRect(x: 0, y: 0, width: CGFloat(pixelW), height: CGFloat(pixelH)))
        cg.scaleBy(x: scale, y: scale)
        cg.translateBy(x: -cropRect.origin.x, y: -cropRect.origin.y)
        page.draw(with: .mediaBox, to: cg)
    }
    NSGraphicsContext.restoreGraphicsState()

    if let pngData = bitmap.representation(using: .png, properties: [:]) {
        try pngData.write(to: URL(fileURLWithPath: spec.outputPath))
        print("[OK] Extracted p.\(spec.pageNumber) -> \(spec.outputPath)")
    }
}
