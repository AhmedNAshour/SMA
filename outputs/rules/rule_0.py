def findDecision(obj): #obj[0]: Fever, obj[1]: Tiredness, obj[2]: Dry-Cough, obj[3]: Difficulty-in-Breathing, obj[4]: Sore-Throat, obj[5]: Pains, obj[6]: Nasal-Congestion, obj[7]: Runny-Nose, obj[8]: Diarrhea, obj[9]: Smell and taste loss
   # {"feature": "Smell and taste loss", "instances": 26739, "metric_value": 0.9507, "depth": 1}
   if obj[9]>0:
      # {"feature": "Nasal-Congestion", "instances": 21960, "metric_value": 0.7836, "depth": 2}
      if obj[6]<=0.0:
         # {"feature": "Pains", "instances": 12848, "metric_value": 0.9702, "depth": 3}
         if obj[5]<=0:
            # {"feature": "Fever", "instances": 7768, "metric_value": 0.7223, "depth": 4}
            if obj[0]<=0:
               # {"feature": "Dry-Cough", "instances": 4451, "metric_value": 0.2723, "depth": 5}
               if obj[2]>0:
                  return 'yes'
               elif obj[2]<=0:
                  # {"feature": "Runny-Nose", "instances": 2150, "metric_value": 0.4586, "depth": 6}
                  if obj[7]<=0:
                     # {"feature": "Sore-Throat", "instances": 1199, "metric_value": 0.6656, "depth": 7}
                     if obj[4]<=0:
                        # {"feature": "Diarrhea", "instances": 805, "metric_value": 0.8243, "depth": 8}
                        if obj[8]>0:
                           # {"feature": "Tiredness", "instances": 404, "metric_value": 0.7422, "depth": 9}
                           if obj[1]<=0:
                              return 'yes'
                           elif obj[1]>0:
                              # {"feature": "Difficulty-in-Breathing", "instances": 194, "metric_value": 0.9889, "depth": 10}
                              if obj[3]<=0:
                                 return 'yes'
                              else:
                                 return 'yes'
                           else:
                              return 'yes'
                        elif obj[8]<=0:
                           # {"feature": "Tiredness", "instances": 401, "metric_value": 0.8894, "depth": 9}
                           if obj[1]<=0:
                              # {"feature": "Difficulty-in-Breathing", "instances": 301, "metric_value": 0.9758, "depth": 10}
                              if obj[3]>0:
                                 return 'yes'
                              elif obj[3]<=0:
                                 return 'yes'
                              else:
                                 return 'yes'
                           elif obj[1]>0:
                              return 'yes'
                           else:
                              return 'yes'
                        else:
                           return 'yes'
                     elif obj[4]>0:
                        return 'yes'
                     else:
                        return 'yes'
                  elif obj[7]>0:
                     return 'yes'
                  else:
                     return 'yes'
               else:
                  return 'yes'
            elif obj[0]>0:
               # {"feature": "Sore-Throat", "instances": 3317, "metric_value": 0.9744, "depth": 5}
               if obj[4]<=0:
                  # {"feature": "Diarrhea", "instances": 1706, "metric_value": 0.395, "depth": 6}
                  if obj[8]>0:
                     # {"feature": "Dry-Cough", "instances": 898, "metric_value": 0.6051, "depth": 7}
                     if obj[2]<=0:
                        # {"feature": "Tiredness", "instances": 512, "metric_value": 0.8264, "depth": 8}
                        if obj[1]>0:
                           # {"feature": "Runny-Nose", "instances": 314, "metric_value": 0.9831, "depth": 9}
                           if obj[7]<=0:
                              # {"feature": "Difficulty-in-Breathing", "instances": 226, "metric_value": 0.9773, "depth": 10}
                              if obj[3]<=0:
                                 return 'no'
                              else:
                                 return 'no'
                           elif obj[7]>0:
                              return 'yes'
                           else:
                              return 'yes'
                        elif obj[1]<=0:
                           return 'yes'
                        else:
                           return 'yes'
                     elif obj[2]>0:
                        return 'yes'
                     else:
                        return 'yes'
                  elif obj[8]<=0:
                     return 'yes'
                  else:
                     return 'yes'
               elif obj[4]>0:
                  # {"feature": "Difficulty-in-Breathing", "instances": 1611, "metric_value": 0.8056, "depth": 6}
                  if obj[3]<=0:
                     return 'no'
                  elif obj[3]>0:
                     return 'yes'
                  else:
                     return 'yes'
               else:
                  return 'no'
            else:
               return 'yes'
         elif obj[5]>0:
            # {"feature": "Runny-Nose", "instances": 5080, "metric_value": 0.8786, "depth": 4}
            if obj[7]<=0:
               # {"feature": "Dry-Cough", "instances": 3284, "metric_value": 0.9921, "depth": 5}
               if obj[2]<=0:
                  # {"feature": "Sore-Throat", "instances": 2459, "metric_value": 0.8302, "depth": 6}
                  if obj[4]<=0:
                     # {"feature": "Fever", "instances": 2259, "metric_value": 0.7159, "depth": 7}
                     if obj[0]<=0:
                        # {"feature": "Difficulty-in-Breathing", "instances": 2088, "metric_value": 0.5608, "depth": 8}
                        if obj[3]<=0:
                           # {"feature": "Tiredness", "instances": 1999, "metric_value": 0.4449, "depth": 9}
                           if obj[1]<=0:
                              # {"feature": "Diarrhea", "instances": 1584, "metric_value": 0.2991, "depth": 10}
                              if obj[8]<=0:
                                 return 'no'
                              else:
                                 return 'no'
                           elif obj[1]>0:
                              # {"feature": "Diarrhea", "instances": 415, "metric_value": 0.8006, "depth": 10}
                              if obj[8]<=0:
                                 return 'no'
                              else:
                                 return 'no'
                           else:
                              return 'no'
                        elif obj[3]>0:
                           return 'yes'
                        else:
                           return 'yes'
                     elif obj[0]>0:
                        return 'yes'
                     else:
                        return 'yes'
                  elif obj[4]>0:
                     return 'yes'
                  else:
                     return 'yes'
               elif obj[2]>0:
                  return 'yes'
               else:
                  return 'yes'
            elif obj[7]>0:
               # {"feature": "Sore-Throat", "instances": 1796, "metric_value": 0.163, "depth": 5}
               if obj[4]>0:
                  # {"feature": "Tiredness", "instances": 1769, "metric_value": 0.0744, "depth": 6}
                  if obj[1]>0:
                     # {"feature": "Difficulty-in-Breathing", "instances": 1758, "metric_value": 0.0282, "depth": 7}
                     if obj[3]<=0:
                        return 'no'
                     elif obj[3]>0:
                        # {"feature": "Diarrhea", "instances": 258, "metric_value": 0.1379, "depth": 8}
                        if obj[8]>0:
                           # {"feature": "Fever", "instances": 254, "metric_value": 0.0371, "depth": 9}
                           if obj[0]<=1:
                              # {"feature": "Dry-Cough", "instances": 254, "metric_value": 0.0371, "depth": 10}
                              if obj[2]<=1:
                                 return 'no'
                              else:
                                 return 'no'
                           else:
                              return 'no'
                        elif obj[8]<=0:
                           return 'yes'
                        else:
                           return 'yes'
                     else:
                        return 'no'
                  elif obj[1]<=0:
                     return 'yes'
                  else:
                     return 'yes'
               elif obj[4]<=0:
                  return 'yes'
               else:
                  return 'yes'
            else:
               return 'no'
         else:
            return 'no'
      elif obj[6]>0.0:
         return 'yes'
      else:
         return 'yes'
   elif obj[9]<=0:
      # {"feature": "Nasal-Congestion", "instances": 4779, "metric_value": 0.0159, "depth": 2}
      if obj[6]<=0.0:
         # {"feature": "Difficulty-in-Breathing", "instances": 4775, "metric_value": 0.0076, "depth": 3}
         if obj[3]<=0:
            # {"feature": "Pains", "instances": 4508, "metric_value": 0.003, "depth": 4}
            if obj[5]>0:
               return 'no'
            elif obj[5]<=0:
               # {"feature": "Sore-Throat", "instances": 1376, "metric_value": 0.0086, "depth": 5}
               if obj[4]>0:
                  return 'no'
               elif obj[4]<=0:
                  # {"feature": "Dry-Cough", "instances": 240, "metric_value": 0.0389, "depth": 6}
                  if obj[2]<=0:
                     return 'no'
                  elif obj[2]>0:
                     return 'yes'
                  else:
                     return 'yes'
               else:
                  return 'no'
            else:
               return 'no'
         elif obj[3]>0:
            # {"feature": "Fever", "instances": 267, "metric_value": 0.0637, "depth": 4}
            if obj[0]>0:
               return 'no'
            elif obj[0]<=0:
               # {"feature": "Dry-Cough", "instances": 65, "metric_value": 0.1982, "depth": 5}
               if obj[2]<=0:
                  # {"feature": "Pains", "instances": 64, "metric_value": 0.1161, "depth": 6}
                  if obj[5]<=0:
                     return 'no'
                  elif obj[5]>0:
                     return 'yes'
                  else:
                     return 'yes'
               elif obj[2]>0:
                  return 'yes'
               else:
                  return 'yes'
            else:
               return 'no'
         else:
            return 'no'
      elif obj[6]>0.0:
         return 'yes'
      else:
         return 'yes'
   else:
      return 'no'
