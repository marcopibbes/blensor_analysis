import open3d as o3d
import numpy as np
import scipy

def associate_detections(tracks, detections):
    iou_matrix = np.zeros((len(tracks), len(detections)))
    for i, track in enumerate(tracks):
        for j, detection in enumerate(detections):
            # Calculate IoU between track and detection bounding boxes
            iou_matrix[i, j] = calculate_iou(track[1], detection)

    # Use a suitable association algorithm like Hungarian algorithm to assign detections to tracks
    assignments = scipy.optimize.linear_sum_assignment(-iou_matrix)[0]
    return assignments

def kalman_filter_tracking(boxes1, boxes2):
    # Assuming boxes are in 3D world coordinates and normalized (0-1 for each dimension)
    # Create Kalman filters for each object track
    kalman_filters = []
    tracks = []  # List to store track IDs and bounding boxes

    for box in boxes1:
        # Initialize Kalman filter for each box
        kalman_filter = o3d.ml.KalmanFilter(state_dim=7, obs_dim=3)  # 7 for 3D position and velocity, 3 for observations
        kalman_filter.set_process_noise(np.diag([0.1, 0.1, 0.1, 0.01, 0.01, 0.01]))  # Adjust noise covariance as needed
        kalman_filter.set_observation_noise(np.diag([0.1, 0.1, 0.1]))  # Adjust noise covariance as needed

        # Initial state: center of the bounding box in 3D world coordinates
        initial_state = np.array([box[0] + box[2] / 2, box[1] + box[3] / 2, box[4] + box[5] / 2, 0, 0, 0])
        kalman_filter.set_state(initial_state)

        # Track ID and bounding box
        track_id = len(tracks)
        tracks.append((track_id, box))

        kalman_filters.append(kalman_filter)

    # Associate detections (boxes2) with existing tracks using bounding box overlap or other criteria
    associations = associate_detections(tracks, boxes2)

    # Update Kalman filters and track boxes
    for i, (track_id, box1) in enumerate(tracks):
        if associations[i] is not None:
            # Get associated detection (box2)
            box2 = boxes2[associations[i]]

            # Update Kalman filter
            kalman_filters[i].predict()
            observation = np.array([box2[0] + box2[2] / 2, box2[1] + box2[3] / 2, box2[4] + box2[5] / 2])
            kalman_filters[i].update(observation)

            # Update track bounding box
            state = kalman_filters[i].get_state()
            tracks[i] = (track_id, [state[0] - state[3] / 2, state[1] - state[4] / 2, state[2] - state[5] / 2,
                                      state[3], state[4], state[5]])  # Un-normalize coordinates

        else:
            # No association found, handle lost tracks (e.g., remove or predict their positions)
            pass  # Implement logic for lost track handling

    return tracks


def visualize_geometry(geometry, track_id):
    # Assign color based on track ID
    color_palette = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1,1,0)]  # Define your desired color palette
    color = color_palette[track_id % len(color_palette)]

    # Set the color of the geometry
    geometry.paint_uniform_color(color)

    return geometry

def calculate_iou(box1, box2):
  """
  Calculates the Intersection-over-Union (IoU) between two bounding boxes.

  Args:
      box1: List of 6 elements representing the first bounding box (xmin, ymin, zmin, xmax, ymax, zmax).
      box2: List of 6 elements representing the second bounding box (xmin, ymin, zmin, xmax, ymax, zmax).

  Returns:
      float: The IoU value between the two bounding boxes.
  """

  # Extract coordinates
  x1_min, y1_min, z1_min, x1_max, y1_max, z1_max = box1
  x2_min, y2_min, z2_min, x2_max, y2_max, z2_max = box2

  # Calculate area of intersection
  intersection_area = max(0, min(x1_max, x2_max) - max(x1_min, x2_min)) * \
                     max(0, min(y1_max, y2_max) - max(y1_min, y2_min)) * \
                     max(0, min(z1_max, z2_max) - max(z1_min, z2_min))

  # Calculate area of each bounding box
  box1_area = (x1_max - x1_min) * (y1_max - y1_min) * (z1_max - z1_min)
  box2_area = (x2_max - x2_min) * (y2_max - y2_min) * (z2_max - z2_min)

  # Calculate and return IoU
  iou = intersection_area / (box1_area + box2_area - intersection_area + 1e-10)  # Add small epsilon to avoid division by zero
  return iou